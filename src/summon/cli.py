"""summon run | score | report"""

import argparse

from dotenv import load_dotenv

from . import LENSES, load_config


def main():
    parser = argparse.ArgumentParser(prog="summon", description=__doc__)
    parser.add_argument("command", choices=["run", "score", "report"])
    parser.add_argument("--config", default="config.yaml")
    parser.add_argument("--lens", action="append", choices=LENSES,
                        help="limit to this lens (repeatable); default: all lenses")
    args = parser.parse_args()

    load_dotenv(".env")  # existing environment variables take precedence
    cfg = load_config(args.config)

    if args.command == "run":
        from .run import main as cmd
    elif args.command == "score":
        from .judge import main as cmd
    else:
        from .report import main as cmd
    cmd(cfg, args.lens)


if __name__ == "__main__":
    main()
