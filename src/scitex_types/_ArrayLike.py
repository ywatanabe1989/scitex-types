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

from scitex_dev import try_import_optional

_np = try_import_optional("numpy", extra="all", pkg="scitex-types")
NUMPY_AVAILABLE = _np is not None

_pd = try_import_optional("pandas", extra="all", pkg="scitex-types")
PANDAS_AVAILABLE = _pd is not None

_xr = try_import_optional("xarray", extra="all", pkg="scitex-types")
XARRAY_AVAILABLE = _xr is not None

_torch = try_import_optional("torch", extra="all", pkg="scitex-types")
TORCH_AVAILABLE = _torch is not None


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
