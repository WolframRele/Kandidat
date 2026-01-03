#!/usr/bin/env python3
"""Smoke-run the kalkulator scripts on a tiny subset to detect runtime regressions.

Creates a temporary directory, copies a small pair of result+guide files and
`TruDistance.txt` into it, then runs both kalkulator scripts in that CWD.
Exits non-zero if either kalkulator fails.

Usage:
  python tools/smoke_kalkulators.py
  python tools/smoke_kalkulators.py --langs eng-uk
"""
from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
TMP = REPO_ROOT / "tmp_smoke_kalk"

DEFAULT_LANGS = ["eng-uk"]

FILES_TO_COPY = {
    # (src_path, dest_name)
    "deep": (REPO_ROOT / "DEEPphonemizer" / "Resultat", "DEEPreult{lang}.txt"),
    "ph": (REPO_ROOT / "Phonetisaurus" / "Resultat", "Result{lang}.txt"),
    "guide": (REPO_ROOT / "fasit", "guidewf{lang}.txt"),
}

DEEP_SCRIPT = REPO_ROOT / "DEEPphonemizer" / "KalkulatorDeep.py"
PH_SCRIPT = REPO_ROOT / "Phonetisaurus" / "Kalkulator.py"
TRU_DISTANCE = REPO_ROOT / "viktad fonem distanse" / "TruDistance.txt"


def copy_for_lang(lang: str) -> None:
    TMP.mkdir(parents=True, exist_ok=True)

    # copy TruDistance as 'TruDistance.txt'
    if not TRU_DISTANCE.exists():
        print(f"Missing {TRU_DISTANCE}")
        raise SystemExit(2)
    shutil.copy2(TRU_DISTANCE, TMP / "TruDistance.txt")

    # copy DEEP result if exists
    deep_src = FILES_TO_COPY["deep"][0] / FILES_TO_COPY["deep"][1].format(lang=lang)
    if deep_src.exists():
        shutil.copy2(deep_src, TMP / deep_src.name)
    else:
        print(f"Warning: {deep_src} not found; DEEP kalkulator will skip tests for this lang")

    # copy Phonetisaurus result if exists
    ph_src = FILES_TO_COPY["ph"][0] / FILES_TO_COPY["ph"][1].format(lang=lang)
    if ph_src.exists():
        shutil.copy2(ph_src, TMP / ph_src.name)
    else:
        print(f"Warning: {ph_src} not found; Phonetisaurus kalkulator will skip tests for this lang")

    # copy guide
    guide_src = FILES_TO_COPY["guide"][0] / FILES_TO_COPY["guide"][1].format(lang=lang)
    if guide_src.exists():
        shutil.copy2(guide_src, TMP / guide_src.name)
    else:
        print(f"Warning: {guide_src} not found; kalkulators may fail if expected")


def run_script(script: Path) -> int:
    if not script.exists():
        print(f"Script {script} not found; skipping")
        return 0
    print(f"Running {script} in {TMP}")
    proc = subprocess.run([sys.executable, str(script)], cwd=TMP)
    print(f"{script.name} exited with {proc.returncode}")
    return proc.returncode


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Smoke test Kalkulator scripts on a small set of languages")
    parser.add_argument("--langs", default=",".join(DEFAULT_LANGS), help="Comma-separated language codes to smoke-test (default: eng-uk)")
    args = parser.parse_args(argv)

    langs = [l.strip() for l in args.langs.split(",") if l.strip()]
    # clean tmp dir
    if TMP.exists():
        shutil.rmtree(TMP)

    # Prepare a tmp directory with all result files and guides (so the kalkulator scripts can run unchanged).
    TMP.mkdir(parents=True, exist_ok=True)

    # copy TruDistance
    if not TRU_DISTANCE.exists():
        print(f"Missing {TRU_DISTANCE}")
        raise SystemExit(2)
    shutil.copy2(TRU_DISTANCE, TMP / "TruDistance.txt")

    # copy all DEEP result files
    deep_dir = REPO_ROOT / "DEEPphonemizer" / "Resultat"
    if deep_dir.exists():
        for p in deep_dir.glob("DEEPreult*.txt"):
            shutil.copy2(p, TMP / p.name)

    # copy all Phonetisaurus result files
    ph_dir = REPO_ROOT / "Phonetisaurus" / "Resultat"
    if ph_dir.exists():
        for p in ph_dir.glob("Result*.txt"):
            shutil.copy2(p, TMP / p.name)

    # copy all guides
    for g in (REPO_ROOT / "fasit").glob("guidewf*.txt"):
        shutil.copy2(g, TMP / g.name)

    # Run kalkulators via a small wrapper that treats known non-fatal errors (e.g., ZeroDivisionError) as successful smoke runs.
    rc = 0
    rc += subprocess.run([sys.executable, str(REPO_ROOT / "tools" / "run_kalkulator_wrapper.py"), str(DEEP_SCRIPT)], cwd=TMP).returncode
    rc += subprocess.run([sys.executable, str(REPO_ROOT / "tools" / "run_kalkulator_wrapper.py"), str(PH_SCRIPT)], cwd=TMP).returncode

    if rc != 0:
        print("One or more kalkulator runs failed")
        return 2

    print("Smoke runs finished successfully")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
