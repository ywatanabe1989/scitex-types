#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File: /home/ywatanabe/proj/scitex-types/tests/examples/test_quickstart.py

"""End-to-end execution test for examples/quickstart.py.

Per scitex-dev PS303 every example must have a matching test under
`tests/examples/`. The meaningful contract: the example **runs**
without raising. Tests that only check `Path.exists()` or `py_compile`
are theater — they pass even when the example imports a removed
symbol or asserts on stale behaviour. We invoke the example in a
real subprocess against the installed `scitex_types`.
"""

import subprocess
import sys
from pathlib import Path

EXAMPLE = Path(__file__).resolve().parents[2] / "examples" / "quickstart.py"


def test_quickstart_runs_end_to_end_without_raising():
    # Arrange
    cmd = [sys.executable, str(EXAMPLE)]
    # Act
    result = subprocess.run(cmd, check=False, capture_output=True, timeout=30)
    # Assert
    assert result.returncode == 0, (
        f"example exited {result.returncode}\n"
        f"stdout:\n{result.stdout.decode(errors='replace')}\n"
        f"stderr:\n{result.stderr.decode(errors='replace')}"
    )


def test_quickstart_prints_expected_is_array_like_marker():
    """The example's print statements are part of its public contract —
    they exercise the documented API and demonstrate the values users
    see when they copy/paste the snippet. Asserting on the marker
    catches accidental rename / removal of the `is_array_like` API."""
    # Arrange
    cmd = [sys.executable, str(EXAMPLE)]
    # Act
    result = subprocess.run(cmd, check=False, capture_output=True, timeout=30)
    stdout = result.stdout.decode(errors="replace")
    # Assert
    assert "is_array_like([1,2,3]):" in stdout


def test_quickstart_prints_expected_is_listed_x_marker():
    # Arrange
    cmd = [sys.executable, str(EXAMPLE)]
    # Act
    result = subprocess.run(cmd, check=False, capture_output=True, timeout=30)
    stdout = result.stdout.decode(errors="replace")
    # Assert
    assert "is_listed_X([1,2,3], int):" in stdout


def test_quickstart_prints_expected_arraylike_alias_marker():
    # Arrange
    cmd = [sys.executable, str(EXAMPLE)]
    # Act
    result = subprocess.run(cmd, check=False, capture_output=True, timeout=30)
    stdout = result.stdout.decode(errors="replace")
    # Assert
    assert "ArrayLike alias:" in stdout
