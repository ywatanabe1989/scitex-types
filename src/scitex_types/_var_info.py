#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time-stamp: "2024-11-25 00:35:31 (ywatanabe)"
# File: ./src/scitex_types/_var_info.py
"""``var_info`` — structural / type info for any variable.

Ported from scitex_gen._var_info (Phase B retirement wave). The upstream
version had hard imports of numpy/pandas/xarray/torch; here we lazy-load
each via scitex_dev.try_import_optional so a minimal install (no torch,
no xarray) still works.
"""

from __future__ import annotations

from typing import Any

from scitex_dev import try_import_optional

_np = try_import_optional("numpy", extra="all", pkg="scitex-types")
_pd = try_import_optional("pandas", extra="all", pkg="scitex-types")
_xr = try_import_optional("xarray", extra="all", pkg="scitex-types")
_torch = try_import_optional("torch", extra="all", pkg="scitex-types")


def _build_array_isinstance_types() -> tuple[type, ...]:
    """Return the tuple of array-like types that are importable."""
    types: list[type] = []
    if _np is not None:
        types.append(_np.ndarray)
    if _pd is not None:
        types.extend([_pd.DataFrame, _pd.Series])
    if _xr is not None:
        types.append(_xr.DataArray)
    if _torch is not None:
        types.append(_torch.Tensor)
    return tuple(types)


_ARRAY_TYPES = _build_array_isinstance_types()


def var_info(variable: Any) -> dict:
    """Returns type and structural information about a variable.

    Example
    -------
    >>> import numpy as np
    >>> data = np.array([[1, 2], [3, 4]])
    >>> info = var_info(data)
    >>> info  # doctest: +ELLIPSIS
    {'type': 'ndarray', 'length': 2, 'shape': (2, 2), 'dimensions': 2}

    Parameters
    ----------
    variable : Any
        Variable to inspect.

    Returns
    -------
    dict
        Dictionary containing variable information.
    """
    info: dict = {"type": type(variable).__name__}

    # Length check
    if hasattr(variable, "__len__"):
        try:
            info["length"] = len(variable)
        except TypeError:  # 0-d arrays etc.
            pass

    # Shape check for array-like objects (only those whose source library
    # is importable in this environment).
    if _ARRAY_TYPES and isinstance(variable, _ARRAY_TYPES):
        info["shape"] = variable.shape
        info["dimensions"] = len(variable.shape)

    # Special handling for nested lists
    elif isinstance(variable, list):
        if variable and isinstance(variable[0], list):
            depth = 1
            current = variable
            shape = [len(variable)]
            while current and isinstance(current[0], list):
                shape.append(len(current[0]))
                current = current[0]
                depth += 1
            info["shape"] = tuple(shape)
            info["dimensions"] = depth

    return info


# EOF
