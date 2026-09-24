"""Run each test as a short conversation and summarize its outcome (spec §5)."""

from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone

import anthropic

from . import (
    LENSES, SCENARIOS, TESTS, Fatal, check_tests_identical, log, require_env,
    result_path, scenario_text, template_path, with_retries, write_json,
)

GUIDANCE_MARKER = "---- follow-up guidance ----"
FINAL_QUESTION = "What should we do?"
QUESTIONER_MAX_TOKENS = 8000
SUMMARY_MAX_TOKENS = 8000

QUESTIONER_PROMPT = """You are playing the user in the conversation below, which is still in
progress. Write the user's next message: one short follow-up question.

{guidance}

Don't ask for a final recommendation yet; that comes later. Reply with only
the question, nothing else.

<conversation>
{transcript}
</conversation>"""

SUMMARY_PROMPT = """Below is a scenario and a conversation about it. Summarize the outcome in
about 250 words of plain prose: what the assistant ultimately recommends
doing, its main reasons, the actions or tests it proposes, and its key
caveats, in the assistant's own terms. Do not describe the conversation, the
questions asked, or how the recommendation developed. Do not evaluate the
recommendation or add ideas it does not contain.

<scenario>
{scenario}
</scenario>

<conversation>
{transcript}
</conversation>"""


def load_test(scenario, lens, test):
    """Return (opening message, follow-up guidance) for a test on a scenario."""
    path = template_path(scenario, lens, test)
    opening, _, guidance = path.read_text().partition(GUIDANCE_MARKER)
    if not guidance.strip():
        raise SystemExit(f"{path} has no '{GUIDANCE_MARKER}' section")
    return opening.replace("{{SCENARIO}}", scenario_text(scenario)).strip(), guidance.strip()


def ask(client, cfg, messages, max_tokens, label=""):
    """One request over the given messages. Returns (text, final_message)."""

    def call():
        try:
            with client.messages.stream(
                model=cfg["subject_model"],
                max_tokens=max_tokens,
                thinking={"type": "adaptive"},
                output_config={"effort": cfg["effort"]},
                messages=messages,
            ) as stream:
                return stream.get_final_message()
        except (anthropic.AuthenticationError, anthropic.PermissionDeniedError,
                anthropic.BadRequestError, anthropic.NotFoundError) as e:
            raise Fatal(f"{type(e).__name__}: {e}") from e

    message = with_retries(call, label=label)
    if message.stop_reason == "max_tokens":
        raise Fatal("cut off by max_tokens")
    if message.stop_reason == "refusal":
        raise Fatal(f"refused ({getattr(message, 'stop_details', None)})")
    text = "\n\n".join(b.text for b in message.content if b.type == "text").strip()
    if not text:
        raise Fatal(f"empty response (stop_reason={message.stop_reason})")
    return text, message


def ask_once(client, cfg, prompt, max_tokens, label=""):
    return ask(client, cfg, [{"role": "user", "content": prompt}], max_tokens, label)


def usage(message):
    u = message.usage
    return {"input_tokens": u.input_tokens, "output_tokens": u.output_tokens}


def now():
    return datetime.now(timezone.utc).isoformat()


def transcript(turns):
    return "\n\n".join(f"User: {t['user']}\n\nAssistant: {t['assistant']}" for t in turns)


def run_test(client, cfg, scenario, lens, test):
    label = f"{scenario}/{lens}/{test}"
    opening, guidance = load_test(scenario, lens, test)
    started = now()
    messages = []
    turns = []
    n_followups = cfg["followups"]

    for i in range(n_followups + 2):
        if i == 0:
            user, question_by = opening, "template"
        elif i <= n_followups:
            user, q_message = ask_once(
                client, cfg,
                QUESTIONER_PROMPT.format(guidance=guidance, transcript=transcript(turns)),
                QUESTIONER_MAX_TOKENS, label,
            )
            question_by = {"model": q_message.model, "usage": usage(q_message)}
        else:
            user, question_by = FINAL_QUESTION, "fixed"
        messages.append({"role": "user", "content": user})
        answer, message = ask(client, cfg, messages, cfg["max_tokens"], label)
        # Send the assistant's full content (thinking included) back unchanged.
        messages.append({"role": "assistant", "content": message.content})
        turns.append({
            "user": user,
            "assistant": answer,
            "question_by": question_by,
            "stop_reason": message.stop_reason,
            "model": message.model,
            "usage": usage(message),
        })
        log(f"{label}: turn {i + 1}/{n_followups + 2} done ({len(answer.split())} words)")

    summary, summary_message = ask_once(
        client, cfg,
        SUMMARY_PROMPT.format(scenario=scenario_text(scenario), transcript=transcript(turns)),
        SUMMARY_MAX_TOKENS, label,
    )
    record = {
        "test_id": label,
        "scenario": scenario,
        "lens": lens,
        "test": test,
        "guidance": guidance,
        "turns": turns,
        "final_answer": turns[-1]["assistant"],
        "summary": summary,
        "model": turns[-1]["model"],
        "summary_usage": usage(summary_message),
        "summary_model": summary_message.model,
        "started_at": started,
        "ended_at": now(),
    }
    path = result_path(scenario, lens, test)
    write_json(path, record)
    body = "\n\n".join(
        f"## Turn {i}\n\n**User:** {t['user']}\n\n**Assistant:**\n\n{t['assistant']}"
        for i, t in enumerate(turns, 1)
    )
    path.with_suffix(".md").write_text(
        f"# {record['test_id']}\n\nModel: {record['model']} · {record['started_at']}\n\n"
        f"{body}\n\n## Outcome summary (sent to Jev)\n\n{summary}\n"
    )
    return record


def main(cfg, lenses=None):
    require_env("ANTHROPIC_API_KEY")
    problems = check_tests_identical()
    if problems:
        raise SystemExit("Test files must be identical across scenarios (they are the control):\n  "
                         + "\n  ".join(problems))
    # Retries are handled by with_retries so a failed stream restarts cleanly.
    client = anthropic.Anthropic(max_retries=0)
    cells = [(s, l, t) for s in SCENARIOS for l in (lenses or LENSES) for t in TESTS]
    todo = [c for c in cells if not result_path(*c).exists()]
    workers = cfg.get("concurrency", 8)
    log(f"{len(cells) - len(todo)} of {len(cells)} tests already done; "
        f"running {len(todo)} with {workers} in parallel")

    failed = []
    done = 0
    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = {pool.submit(run_test, client, cfg, *c): "/".join(c) for c in todo}
        for f in as_completed(futures):
            test_id = futures[f]
            try:
                record = f.result()
            except Fatal as e:
                if "AuthenticationError" in str(e) or "PermissionDeniedError" in str(e):
                    pool.shutdown(cancel_futures=True)
                    raise SystemExit(f"{test_id}: {e}\nCheck ANTHROPIC_API_KEY.")
                failed.append((test_id, str(e)))
                log(f"{test_id}: FAILED: {e}")
                continue
            except Exception as e:
                failed.append((test_id, f"{type(e).__name__}: {e}"))
                log(f"{test_id}: FAILED after retries: {type(e).__name__}: {e}")
                continue
            done += 1
            log(f"{test_id}: ok [{done}/{len(todo)}] final answer "
                f"{len(record['final_answer'].split())} words, summary {len(record['summary'].split())} words")
    if failed:
        log(f"\n{len(failed)} test(s) failed; run `summon run` again to retry them:")
        for test_id, reason in failed:
            log(f"  {test_id}: {reason}")
    else:
        log("\nAll tests complete.")
