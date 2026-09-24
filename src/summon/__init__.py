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


def scenario_files():
    """Map scenario name -> file, from experiments/###-<name>.md, in numeric order."""
    files = sorted(EXPERIMENTS.glob("[0-9][0-9][0-9]-*.md"))
    return {f.stem.split("-", 1)[1]: f for f in files}


def lens_dirs():
    """Each subfolder of experiments/ holding testA–E.md is a lens (one experiment)."""
    return sorted(d.name for d in EXPERIMENTS.iterdir()
                  if d.is_dir() and all((d / f"{t}.md").exists() for t in TESTS))


SCENARIOS = list(scenario_files())
LENSES = lens_dirs()


def load_config(path="config.yaml"):
    with open(path) as f:
        return yaml.safe_load(f)


def require_env(name):
    value = os.environ.get(name)
    if not value:
        raise SystemExit(f"{name} is not set (add it to the environment or .env)")
    return value


def scenario_text(scenario):
    return scenario_files()[scenario].read_text().strip()


def template_path(lens, test):
    return EXPERIMENTS / lens / f"{test}.md"


def result_path(lens, scenario, test):
    return RESULTS / lens / scenario / f"{test}.json"


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
