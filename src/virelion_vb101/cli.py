"""Command-line interface for the VB-101 research scaffold."""

from __future__ import annotations

import argparse
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(
        prog="vb101",
        description="VB-101 computational discovery and prioritization scaffold",
    )
    subparsers = parser.add_subparsers(dest="command")

    run = subparsers.add_parser("run", help="prepare/run the configured discovery workflow")
    run.add_argument("--config", type=Path, required=True, help="path to discovery YAML")

    args = parser.parse_args()
    if args.command is None:
        parser.print_help()
        return 0

    if args.command == "run":
        if not args.config.exists():
            parser.error(f"configuration file does not exist: {args.config}")
        print("VB-101 pipeline scaffold: configuration accepted.")
        print("Analysis modules are intentionally not represented as completed biological results.")
        return 0

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
