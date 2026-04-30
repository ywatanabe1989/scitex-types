#!/usr/bin/env python3
# Timestamp: "2026-04-30 (ywatanabe)"
# File: src/scitex_types/_ArrayLike.py

"""SciTeX-owned ArrayLike type — wider than `numpy.typing.ArrayLike`.

The union covers every array container scitex consumes (lists/tuples + the
optional scientific stack: numpy, pandas, xarray, torch). Each member is
included only when its source library is importable, so a minimal install
(no torch, no xarray) still produces a valid `ArrayLike`.

Both the type alias and the `is_array_like()` runtime check are driven by
the same `_array_types` list so they cannot diverge.
"""

from __future__ import annotations

from typing import List as _List
from typing import Tuple as _Tuple
from typing import Union as _Union

try:
    import numpy as _np

    NUMPY_AVAILABLE = True
except ImportError:
    NUMPY_AVAILABLE = False
    _np = None

try:
    import pandas as _pd

    PANDAS_AVAILABLE = True
except ImportError:
    PANDAS_AVAILABLE = False
    _pd = None

try:
    import xarray as _xr

    XARRAY_AVAILABLE = True
except ImportError:
    XARRAY_AVAILABLE = False
    _xr = None

try:
    import torch as _torch

    TORCH_AVAILABLE = True
except ImportError:
    TORCH_AVAILABLE = False
    _torch = None


# Build the union once; reuse for both the type alias and the runtime check.
_array_types: list[type] = [_List, _Tuple]
if NUMPY_AVAILABLE and _np is not None:
    _array_types.append(_np.ndarray)
if PANDAS_AVAILABLE and _pd is not None:
    _array_types.extend([_pd.Series, _pd.DataFrame])
if XARRAY_AVAILABLE and _xr is not None:
    _array_types.append(_xr.DataArray)
if TORCH_AVAILABLE and _torch is not None:
    _array_types.append(_torch.Tensor)

ArrayLike = _Union[tuple(_array_types)]

# Concrete (non-typing) tuple used by isinstance() — drop _List / _Tuple
# typing aliases and substitute their builtin equivalents.
_runtime_array_types: tuple[type, ...] = tuple(
    list if t is _List else tuple if t is _Tuple else t for t in _array_types
)


def is_array_like(obj) -> bool:
    """Check if object is array-like.

    Returns
    -------
        bool: True if object is array-like, False otherwise.
    """
    try:
        return isinstance(obj, _runtime_array_types)
    except TypeError:
        return False


# EOF
