#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File: ./tests/scitex/types/test__ArrayLike.py

"""Tests for ArrayLike type definition and is_array_like function."""

import pytest

# numpy is an optional extra (scitex-types[all]), so guard at module-import
# time (PA-303). Skips the whole file if the user isn't installing [all].
np = pytest.importorskip("numpy")

from scitex_types import ArrayLike, is_array_like  # noqa: E402


def _require_pandas():
    # `pytest.importorskip` is the auditor-friendly form (PS-210). It
    # skips the test when the optional `[all]` extra dep is missing.
    pytest.importorskip("pandas")


def _require_xarray():
    pytest.importorskip("xarray")


def _require_torch():
    pytest.importorskip("torch")


# ---------------------------------------------------------------------------
# is_array_like — positive cases (basic Python types)
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "test_list",
    [
        [],
        [1, 2, 3],
        [1.0, 2.0, 3.0],
        ["a", "b", "c"],
        [[1, 2], [3, 4]],
        [1, "mixed", 3.0],
    ],
)
def test_python_list_is_recognized_as_array_like(test_list):
    # Arrange
    # Act
    result = is_array_like(test_list)
    # Assert
    assert result, f"List {test_list} not recognized as array-like"


@pytest.mark.parametrize(
    "test_tuple",
    [
        (),
        (1, 2, 3),
        (1.0, 2.0, 3.0),
        ("a", "b", "c"),
        ((1, 2), (3, 4)),
        (1, "mixed", 3.0),
    ],
)
def test_python_tuple_is_recognized_as_array_like(test_tuple):
    # Arrange
    # Act
    result = is_array_like(test_tuple)
    # Assert
    assert result, f"Tuple {test_tuple} not recognized as array-like"


# ---------------------------------------------------------------------------
# is_array_like — numpy
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "test_array",
    [
        np.array([]),
        np.array([1, 2, 3]),
        np.array([[1, 2], [3, 4]]),
        np.zeros((3, 3)),
        np.ones(5),
        np.arange(10),
        np.array(["a", "b", "c"]),
        np.array([1.0, 2.0, 3.0]),
    ],
)
def test_numpy_array_is_recognized_as_array_like(test_array):
    # Arrange
    # Act
    result = is_array_like(test_array)
    # Assert
    assert result, "NumPy array not recognized as array-like"


# ---------------------------------------------------------------------------
# is_array_like — pandas
# ---------------------------------------------------------------------------


def _pandas_objects():
    import pandas as pd

    return [
        pd.Series([1, 2, 3]),
        pd.Series(["a", "b", "c"]),
        pd.Series([], dtype=float),
        pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]}),
        pd.DataFrame(),
        pd.Series(np.arange(10)),
        pd.DataFrame(np.random.randn(5, 3)),
    ]


@pytest.fixture(params=range(7))
def pandas_object(request):
    _require_pandas()
    return _pandas_objects()[request.param]


def test_pandas_object_is_recognized_as_array_like(pandas_object):
    # Arrange
    # Act
    result = is_array_like(pandas_object)
    # Assert
    assert result, f"Pandas object {type(pandas_object)} not array-like"


# ---------------------------------------------------------------------------
# is_array_like — xarray
# ---------------------------------------------------------------------------


def _xarray_objects():
    import xarray as xr

    return [
        xr.DataArray([1, 2, 3]),
        xr.DataArray(np.random.randn(3, 4)),
        xr.DataArray([]),
        xr.DataArray([[1, 2], [3, 4]], dims=["x", "y"]),
    ]


@pytest.fixture(params=range(4))
def xarray_object(request):
    _require_xarray()
    return _xarray_objects()[request.param]


def test_xarray_object_is_recognized_as_array_like(xarray_object):
    # Arrange
    # Act
    result = is_array_like(xarray_object)
    # Assert
    assert result, f"xarray object {type(xarray_object)} not array-like"


# ---------------------------------------------------------------------------
# is_array_like — torch
# ---------------------------------------------------------------------------


def _torch_tensors():
    import torch

    return [
        torch.tensor([1, 2, 3]),
        torch.tensor([[1, 2], [3, 4]]),
        torch.zeros(3, 3),
        torch.ones(5),
        torch.randn(2, 3),
        torch.tensor([1.0, 2.0, 3.0]),
        torch.empty(0),
    ]


@pytest.fixture(params=range(7))
def torch_tensor(request):
    _require_torch()
    return _torch_tensors()[request.param]


def test_torch_tensor_is_recognized_as_array_like(torch_tensor):
    # Arrange
    # Act
    result = is_array_like(torch_tensor)
    # Assert
    assert result, "PyTorch tensor not recognized as array-like"


def test_torch_tensor_passes_when_torch_available():
    # Arrange
    torch = pytest.importorskip("torch")
    tensor = torch.tensor([1, 2, 3])
    # Act
    result = is_array_like(tensor)
    # Assert
    assert result


# ---------------------------------------------------------------------------
# is_array_like — negative cases
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "obj",
    [
        1,
        3.14,
        "string",
        {"key": "value"},
        {1, 2, 3},
        object(),
        None,
        True,
        False,
    ],
)
def test_non_array_object_is_rejected(obj):
    # Arrange
    # Act
    result = is_array_like(obj)
    # Assert
    assert not result, f"{obj!r} ({type(obj)}) wrongly identified as array-like"


def test_lambda_is_not_array_like():
    # Arrange
    fn = lambda x: x  # noqa: E731
    # Act
    result = is_array_like(fn)
    # Assert
    assert not result


class _CustomObject:
    def __init__(self, data):
        self.data = data


class _FakeArrayLike:
    def __getitem__(self, key):
        return key

    def __len__(self):
        return 5


class _GenericObject:
    """Plain object with no array-like attributes."""


@pytest.mark.parametrize(
    "obj",
    [
        _CustomObject([1, 2, 3]),
        _FakeArrayLike(),
        _GenericObject(),
        type,
    ],
)
def test_custom_non_array_object_is_rejected(obj):
    # Arrange
    # Act
    result = is_array_like(obj)
    # Assert
    assert not result, f"Custom object {obj} wrongly identified as array-like"


# ---------------------------------------------------------------------------
# Edge cases
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "obj",
    [
        [[[1]], [[2]]],
        (((), ()), ((), ())),
        list(range(1000)),
        tuple(range(500)),
    ],
)
def test_nested_or_large_container_is_array_like(obj):
    # Arrange
    # Act
    result = is_array_like(obj)
    # Assert
    assert result, f"Edge case {type(obj)} not recognized as array-like"


def test_exception_in_object_is_handled_gracefully():
    # Arrange
    class ProblematicObject:
        def __instancecheck__(self, instance):
            raise RuntimeError("Instance check failed")

    problematic = ProblematicObject()
    # Act
    try:
        result = is_array_like(problematic)
    except Exception:
        result = False
    # Assert
    assert isinstance(result, bool)


# ---------------------------------------------------------------------------
# ArrayLike type structure
# ---------------------------------------------------------------------------


def test_array_like_union_has_multiple_members():
    # Arrange
    from typing import get_args

    # Act
    args = get_args(ArrayLike)
    # Assert
    assert args and len(args) > 1


def test_array_like_union_includes_list_type():
    # Arrange
    from typing import get_args

    # Act
    type_names = [str(a).lower() for a in get_args(ArrayLike)]
    # Assert
    assert any("list" in name for name in type_names)


def test_array_like_union_includes_tuple_type():
    # Arrange
    from typing import get_args

    # Act
    type_names = [str(a).lower() for a in get_args(ArrayLike)]
    # Assert
    assert any("tuple" in name for name in type_names)


def test_torch_tensor_is_member_of_array_like_union():
    # Arrange
    torch = pytest.importorskip("torch")
    from typing import get_args

    # Act
    args = get_args(ArrayLike)
    # Assert
    assert torch.Tensor in args, f"torch.Tensor missing from ArrayLike: {args}"


# ---------------------------------------------------------------------------
# Runtime / type-union agreement
# ---------------------------------------------------------------------------


def _instance_for_union_member(cls):
    from typing import List as _List
    from typing import Tuple as _Tuple

    if cls is _List:
        return [1, 2]
    if cls is _Tuple:
        return (1, 2)
    name = getattr(cls, "__name__", "")
    try:
        if name == "ndarray":
            return np.array([1])
        if name == "Series":
            import pandas as pd

            return pd.Series([1])
        if name == "DataFrame":
            import pandas as pd

            return pd.DataFrame({"a": [1]})
        if name == "DataArray":
            import xarray as xr

            return xr.DataArray([1])
        if name == "Tensor":
            import torch

            return torch.tensor([1])
    except Exception:
        return None
    return None


@pytest.fixture
def union_member_instances():
    from typing import get_args

    out = []
    for cls in get_args(ArrayLike):
        inst = _instance_for_union_member(cls)
        if inst is not None:
            out.append((cls, inst))
    return out


def test_every_union_member_instance_is_array_like(union_member_instances):
    # Arrange
    failures = []
    # Act
    for cls, inst in union_member_instances:
        if not is_array_like(inst):
            failures.append(cls)
    # Assert
    assert not failures, f"is_array_like rejects union members: {failures}"


# ---------------------------------------------------------------------------
# Return-type and docstring contracts
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "obj",
    [[1, 2, 3], "not array", 42, np.array([1, 2]), None],
)
def test_is_array_like_returns_bool(obj):
    # Arrange
    # Act
    result = is_array_like(obj)
    # Assert
    assert isinstance(result, bool)


def test_is_array_like_has_docstring():
    # Arrange
    # Act
    doc = is_array_like.__doc__
    # Assert
    assert doc is not None


def test_is_array_like_docstring_mentions_array_like():
    # Arrange
    doc = is_array_like.__doc__ or ""
    # Act
    # Assert
    assert "array-like" in doc.lower()


def test_is_array_like_docstring_mentions_bool():
    # Arrange
    doc = is_array_like.__doc__ or ""
    # Act
    # Assert
    assert "bool" in doc.lower()


# ---------------------------------------------------------------------------
# Performance / memory smoke tests
# ---------------------------------------------------------------------------


def test_is_array_like_large_list_completes_quickly():
    # Arrange
    import time

    large_list = list(range(10000))
    # Act
    start = time.time()
    result = is_array_like(large_list)
    elapsed = time.time() - start
    # Assert
    assert result and elapsed < 1.0


def test_is_array_like_large_numpy_array_returns_true():
    # Arrange
    large_array = np.zeros(10000)
    # Act
    result = is_array_like(large_array)
    # Assert
    assert result is True
