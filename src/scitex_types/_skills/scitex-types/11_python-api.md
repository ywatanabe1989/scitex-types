---
description: |
  [TOPIC] Python API
  [DETAILS] All public type aliases (ArrayLike, ColorLike) and runtime predicates (is_array_like, is_list_of_type, is_listed_X) with signatures.
tags: [scitex-types-python-api]
---

<!-- 02_python-api.md -->

# scitex-types — Python API

Public surface (from `scitex_types.__all__`):

| Symbol | Kind | One-liner |
|--------|------|-----------|
| `ArrayLike` | type alias | Union of array-ish types (list, tuple, np.ndarray, torch.Tensor, pandas Series/DataFrame, xarray). |
| `ColorLike` | type alias | Union of matplotlib color specs (str name, hex, RGB/RGBA tuple). |
| `is_array_like` | predicate | Runtime check that a value is an `ArrayLike`. |
| `is_listed_X` | predicate | True iff every element of the list is an instance of `X` (type or tuple of types). |
| `is_list_of_type` | predicate | Alias/companion of `is_listed_X` for list-of-type checks. |

## Signatures

```python
is_array_like(obj: Any) -> bool
is_listed_X(seq: Any, X: type | tuple[type, ...]) -> bool
is_list_of_type(seq: Any, X: type | tuple[type, ...]) -> bool
```

The aliases `ArrayLike` and `ColorLike` are defined in
`scitex_types/_ArrayLike.py` and `_ColorLike.py`. Inspect those files for the
exact union members; scitex-types intentionally keeps this tight.
