"""Summon experiment: compare prompting styles with a Jev preference judge."""

import json
import os
import threading
import time
from pathlib import Path

import yaml

TESTS = ["testA", "testB", "testC", "testD", "testE"]
CROSS_LENS_TEST = "testD"   # the "method enacted" condition compared across lenses

EXPERIMENTS = Path("experiments")
RESULTS = Path("results")

_print_lock = threading.Lock()


def log(*parts):
    """Thread-safe print so parallel workers don't interleave within a line."""
    with _print_lock:
        print(*parts, flush=True)


def scenario_dirs():
    """Map scenario name -> folder, from experiments/###-<name>/, in numeric order."""
    dirs = sorted(d for d in EXPERIMENTS.glob("[0-9][0-9][0-9]-*") if d.is_dir())
    return {d.name.split("-", 1)[1]: d for d in dirs}


def lens_names():
    """Lenses are the subfolders of each scenario that hold testA–E.md."""
    found = set()
    for d in scenario_dirs().values():
        found |= {l.name for l in d.iterdir()
                  if l.is_dir() and all((l / f"{t}.md").exists() for t in TESTS)}
    return sorted(found)


SCENARIOS = list(scenario_dirs())
LENSES = lens_names()


def check_tests_identical():
    """The tests are the control: each lens's test files must be identical in every
    scenario. Returns a list of problems (empty if all copies match)."""
    problems = []
    dirs = scenario_dirs()
    for lens in LENSES:
        for test in TESTS:
            versions = {}
            for name, d in dirs.items():
                f = d / lens / f"{test}.md"
                if not f.exists():
                    problems.append(f"missing {f}")
                    continue
                versions.setdefault(f.read_text(), []).append(name)
            if len(versions) > 1:
                groups = "; ".join(", ".join(v) for v in versions.values())
                problems.append(f"{lens}/{test}.md differs between scenarios ({groups})")
    return problems


def load_config(path="config.yaml"):
    with open(path) as f:
        return yaml.safe_load(f)


def require_env(name):
    value = os.environ.get(name)
    if not value:
        raise SystemExit(f"{name} is not set (add it to the environment or .env)")
    return value


def scenario_text(scenario):
    return (scenario_dirs()[scenario] / "scenario.md").read_text().strip()


def template_path(scenario, lens, test):
    return scenario_dirs()[scenario] / lens / f"{test}.md"


def result_path(scenario, lens, test):
    return RESULTS / scenario / lens / f"{test}.json"


def read_json(path):
    return json.loads(Path(path).read_text())


def write_json(path, data):
    """Write via a temp file so a crash never leaves a half-written result."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(data, indent=2, ensure_ascii=False))
    tmp.replace(path)


class Fatal(Exception):
    """A failure that retrying won't fix."""


def with_retries(fn, attempts=4, base_delay=5.0, label=""):
    """Call fn, retrying up to `attempts` times total with exponential backoff."""
    for attempt in range(1, attempts + 1):
        try:
            return fn()
        except Fatal:
            raise
        except Exception as e:
            if attempt == attempts:
                raise
            delay = base_delay * 2 ** (attempt - 1)
            log(f"{label}    attempt {attempt} failed ({type(e).__name__}: {e}); retrying in {delay:.0f}s")
            time.sleep(delay)
