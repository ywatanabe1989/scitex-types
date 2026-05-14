"""PS-140 cross-package import runtime gate.

`src/scitex_types/_ArrayLike.py` imports `scitex_dev.try_import_optional`
to gate the optional numpy/pandas/xarray/torch members of the ArrayLike
union. This file runs that import path end-to-end so a missing or renamed
upstream surface fails CI immediately (instead of at user import time).

Keep `CROSS_PACKAGE_IMPORTS` in sync with the audit-project PS-140 check;
regenerate via `scitex-dev ecosystem write-integration-tests` if drift
appears.
"""

from __future__ import annotations

import importlib

CROSS_PACKAGE_IMPORTS: list[str] = [
    "scitex_dev",
]


def test_cross_package_imports_resolve() -> None:
    """Every declared cross-package import must be importable at test time."""
    for name in CROSS_PACKAGE_IMPORTS:
        importlib.import_module(name)
