#!/usr/bin/env python3
"""Create a Claude-ready club project from templates and examples.

Stdlib-only on purpose.
"""
from __future__ import annotations

import argparse
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEMPLATES = ROOT / "templates"
EXAMPLES = ROOT / "examples"


def available_examples() -> list[str]:
    return sorted(p.name for p in EXAMPLES.iterdir() if p.is_dir())


def safe_name(name: str) -> str:
    cleaned = "".join(ch if ch.isalnum() or ch in "-_" else "-" for ch in name.strip().lower())
    cleaned = "-".join(part for part in cleaned.split("-") if part)
    if not cleaned:
        raise ValueError("project name cannot be empty")
    return cleaned


def copy_tree(src: Path, dst: Path) -> None:
    for item in src.rglob("*"):
        if item.is_dir():
            continue
        rel = item.relative_to(src)
        target = dst / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(item, target)


def create_project(name: str, example: str, out: Path, force: bool = False) -> Path:
    project = out / safe_name(name)
    example_dir = EXAMPLES / example
    if not example_dir.is_dir():
        raise ValueError(f"unknown example: {example}")
    if project.exists() and any(project.iterdir()) and not force:
        raise FileExistsError(f"target project already exists and is not empty: {project}")
    project.mkdir(parents=True, exist_ok=True)
    copy_tree(TEMPLATES, project)
    copy_tree(example_dir, project)
    return project


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a Claude-ready club project")
    parser.add_argument("name", nargs="?", help="new project name")
    parser.add_argument("--example", default="event-announcement-pack", help="example to copy")
    parser.add_argument("--out", default="./work", help="output directory")
    parser.add_argument("--force", action="store_true", help="overwrite files in an existing project folder")
    parser.add_argument("--list", action="store_true", help="list available examples")
    args = parser.parse_args()

    if args.list:
        for example in available_examples():
            print(example)
        return 0

    if not args.name:
        parser.error("name is required unless --list is used")

    try:
        project = create_project(args.name, args.example, Path(args.out), force=args.force)
    except (ValueError, FileExistsError) as exc:
        parser.exit(2, f"error: {exc}\n")
    print(project)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
