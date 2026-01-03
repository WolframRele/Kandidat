#!/usr/bin/env python3
"""Validate presence/size of critical input files and optionally clean generated outputs.

Usage examples:
  python tools/validate_inputs.py --check
  python tools/validate_inputs.py --clean --yes

Checks (defaults, relative to repo root):
- viktad fonem distanse/TruDistance.txt
- DEEPphonemizer/data.txt
- DEEPphonemizer/config.yaml
- guidewf*.txt (in DEEPphonemizer/, DEEPphonemizer/Test data/ or top-level `fasit/`)

Cleaning removes common generated outputs like:
- DEEPphonemizer/Resultat/DEEPreult*.txt
- Phonetisaurus/Resultat/Result*.txt
- guide*.txt and guidewf*.txt in repo root (only if --clean-root is set)
"""
from __future__ import annotations

import argparse
import glob
import os
import sys
from pathlib import Path
from typing import List

REPO_ROOT = Path(__file__).resolve().parents[1]

CRITICAL_FILES = [
    REPO_ROOT / "viktad fonem distanse" / "TruDistance.txt",
    REPO_ROOT / "DEEPphonemizer" / "data.txt",
    REPO_ROOT / "DEEPphonemizer" / "config.yaml",
]

GUIDE_LOCATIONS = [
    REPO_ROOT / "DEEPphonemizer",
    REPO_ROOT / "DEEPphonemizer" / "Test data",
    REPO_ROOT / "fasit",
]

CLEAN_PATTERNS = [
    str(REPO_ROOT / "DEEPphonemizer" / "Resultat" / "DEEPreult*.txt"),
    str(REPO_ROOT / "Phonetisaurus" / "Resultat" / "Result*.txt"),
    str(REPO_ROOT / "DEEPphonemizer" / "DEEPreult*.txt"),
    str(REPO_ROOT / "Phonetisaurus" / "Result*.txt"),
]

ROOT_CLEAN_PATTERNS = [
    str(REPO_ROOT / "guide*.txt"),
    str(REPO_ROOT / "guidewf*.txt"),
]


def find_guides() -> List[Path]:
    found = []
    for loc in GUIDE_LOCATIONS:
        if loc.exists() and loc.is_dir():
            for p in loc.glob("guidewf*.txt"):
                found.append(p)
    return found


def check_critical_files() -> List[Path]:
    missing = []
    zero_size = []
    for p in CRITICAL_FILES:
        if not p.exists():
            missing.append(p)
        else:
            if p.stat().st_size == 0:
                zero_size.append(p)
    return missing, zero_size


def list_matches(patterns: List[str]) -> List[Path]:
    files = []
    for pat in patterns:
        for p in glob.glob(pat):
            files.append(Path(p))
    return files


def safe_delete(paths: List[Path], yes: bool = False) -> List[Path]:
    deleted = []
    if not paths:
        return deleted
    if not yes:
        print("About to delete the following files:")
        for p in paths:
            print("  ", p)
        resp = input("Proceed? [y/N]: ")
        if resp.strip().lower() != "y":
            print("Aborting deletion.")
            return deleted
    for p in paths:
        try:
            p.unlink()
            deleted.append(p)
        except Exception as e:
            print(f"Failed to delete {p}: {e}")
    return deleted


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Validate repository inputs and optionally clean outputs.")
    parser.add_argument("--check", action="store_true", help="Run checks (default)" )
    parser.add_argument("--clean", action="store_true", help="Delete generated output files (safe prompt)" )
    parser.add_argument("--clean-root", action="store_true", help="Include root guide files when cleaning (risky)")
    parser.add_argument("--yes", action="store_true", help="Assume yes for deletions")
    args = parser.parse_args(argv)

    # Default to check if nothing else
    if not (args.check or args.clean):
        args.check = True

    ok = True

    if args.check:
        print("Checking critical files...")
        missing, zero_size = check_critical_files()
        if missing:
            ok = False
            print("Missing critical files:")
            for p in missing:
                print("  -", p)
        if zero_size:
            ok = False
            print("Critical files with zero size:")
            for p in zero_size:
                print("  -", p)

        guides = find_guides()
        if not guides:
            ok = False
            print("No guidewf*.txt found in expected locations:")
            for loc in GUIDE_LOCATIONS:
                print("  -", loc)
        else:
            print(f"Found {len(guides)} guidewf files; example: {guides[0]}")

        print("Scanning for generated result files (not an error, for info):")
        found_results = list_matches(CLEAN_PATTERNS)
        if found_results:
            for p in found_results:
                print("  ", p)
        else:
            print("  None found")

        if ok:
            print("All checks passed.")
        else:
            print("One or more checks failed. Fix the issues and re-run.")

    if args.clean:
        patterns = CLEAN_PATTERNS.copy()
        if args.clean_root:
            patterns += ROOT_CLEAN_PATTERNS
        to_delete = list_matches(patterns)
        if not to_delete:
            print("No files matched clean patterns.")
        else:
            deleted = safe_delete(to_delete, yes=args.yes)
            print(f"Deleted {len(deleted)} files.")

    return 0 if ok else 2


if __name__ == "__main__":
    raise SystemExit(main())
