#!/usr/bin/env python3
# Timestamp: "2025-05-01 09:21:23 (ywatanabe)"
# File: src/scitex_types/_ArrayLike.py

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


def _get_torch_tensor_type():
    """Lazily import torch.Tensor to avoid circular imports."""
    try:
        import torch

        return torch.Tensor
    except (ImportError, RuntimeError):
        return type(None)


# Build ArrayLike union dynamically based on available packages
_array_types = [_List, _Tuple]
if NUMPY_AVAILABLE:
    _array_types.append(_np.ndarray)
if PANDAS_AVAILABLE:
    _array_types.extend([_pd.Series, _pd.DataFrame])
if XARRAY_AVAILABLE:
    _array_types.append(_xr.DataArray)

ArrayLike = _Union[tuple(_array_types)]


def is_array_like(obj) -> bool:
    """Check if object is array-like.

    Returns
    -------
        bool: True if object is array-like, False otherwise.
    """
    base_types = [_List, _Tuple]
    if NUMPY_AVAILABLE:
        base_types.append(_np.ndarray)
    if PANDAS_AVAILABLE:
        base_types.extend([_pd.Series, _pd.DataFrame])
    if XARRAY_AVAILABLE:
        base_types.append(_xr.DataArray)

    if isinstance(obj, tuple(base_types)):
        return True

    # Check torch tensor lazily to avoid circular imports
    try:
        import torch

        return torch.is_tensor(obj)
    except (ImportError, RuntimeError):
        return False


# EOF
