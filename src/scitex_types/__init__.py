#!/usr/bin/env python3
"""scitex-types: Scientific type definitions and validation."""

from __future__ import annotations

from importlib.metadata import PackageNotFoundError
from importlib.metadata import version as _v

try:
    __version__ = _v("scitex-types")
except PackageNotFoundError:
    __version__ = "0.0.0+local"
del _v, PackageNotFoundError

from ._ArrayLike import ArrayLike, is_array_like
from ._ColorLike import ColorLike
from ._is_listed_X import is_list_of_type, is_listed_X

__all__ = [
    "__version__",
    "ArrayLike",
    "ColorLike",
    "is_array_like",
    "is_list_of_type",
    "is_listed_X",
]
