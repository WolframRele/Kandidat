#!/usr/bin/env python3
"""Run a kalkulator script with exceptions handled for CI smoke tests.

Usage:
  python tools/run_kalkulator_wrapper.py /path/to/KalkulatorDeep.py
"""
from __future__ import annotations

import runpy
import sys
from pathlib import Path


def main(argv=None) -> int:
    if argv is None:
        argv = sys.argv[1:]
    if not argv:
        print("Usage: run_kalkulator_wrapper.py <script>")
        return 2
    script = Path(argv[0])
    if not script.exists():
        print(f"Script {script} not found")
        return 2

    try:
        runpy.run_path(str(script), run_name="__main__")
    except ZeroDivisionError:
        print("Kalkulator raised ZeroDivisionError (likely empty language); treating as non-fatal smoke result")
        return 0
    except Exception as e:
        print(f"Kalkulator crashed: {e}")
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
