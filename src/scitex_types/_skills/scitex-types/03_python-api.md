---
description: |
  [TOPIC] scitex-types Python API
  [DETAILS] Public callables — ArrayLike, ColorLike type aliases plus is_array_like, is_list_of_type, is_listed_X predicates.
tags: [scitex-types-python-api]
---

# Python API

## Imports

```python
from scitex_types import (
    ArrayLike,
    ColorLike,
    is_array_like,
    is_list_of_type,
    is_listed_X,
)
```

## Type aliases

| Symbol      | Resolves to                                                 |
|-------------|-------------------------------------------------------------|
| `ArrayLike` | Union over `numpy.ndarray`, `pandas.Series/DataFrame`, `torch.Tensor`, `xarray.DataArray`, `list`, `tuple` (libraries opt-in via extras; missing libs are skipped) |
| `ColorLike` | Union over `str` (named / `#rrggbb`), `tuple[float, float, float]`, `tuple[float, float, float, float]` |

Use these as type hints; they do not enforce at runtime.

## Predicates

### `is_array_like(x) -> bool`

Returns `True` when `x` is one of the array-shaped types in `ArrayLike`.
Conservative: returns `False` for plain scalars and strings.

### `is_list_of_type(seq, expected_type) -> bool`

Returns `True` when `seq` is a list/tuple and **every** element is an
instance of `expected_type`. Empty sequences return `True`.

### `is_listed_X(seq, X) -> bool`

Alias for `is_list_of_type` kept for backwards compatibility with older
SciTeX code.

```python
is_listed_X(["a", "b"], str)         # True
is_listed_X([np.zeros(3)] * 4, np.ndarray)  # True
```

## Two import paths

```python
import scitex_types        # standalone
import scitex.types        # umbrella (requires `pip install scitex`)
```

Both expose the same `__all__`.
