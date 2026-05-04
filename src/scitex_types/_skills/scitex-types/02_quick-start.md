---
description: |
  [TOPIC] scitex-types Quick start
  [DETAILS] Type-hint with ArrayLike / ColorLike, runtime-check with is_array_like and is_listed_X.
tags: [scitex-types-quick-start]
---

# Quick Start

## Type-hint a polymorphic array argument

```python
from scitex_types import ArrayLike

def normalize(x: ArrayLike) -> ArrayLike:
    """Accepts numpy / pandas / torch / xarray and lists/tuples."""
    ...
```

## Runtime-check array-likeness

```python
from scitex_types import is_array_like

if not is_array_like(x):
    raise TypeError(f"expected array-like, got {type(x).__name__}")
```

## Validate a list is uniform

```python
from scitex_types import is_listed_X

assert is_listed_X([1, 2, 3], int)
assert is_listed_X(["a", "b"], str)
assert not is_listed_X([1, "two"], int)
```

## Type-hint a matplotlib color

```python
from scitex_types import ColorLike

def draw(color: ColorLike) -> None:
    """Accepts '#rrggbb', named color, RGB tuple, or RGBA tuple."""
    ...
```

## Next

- [03_python-api.md](03_python-api.md) — every public symbol
- [SKILL.md](SKILL.md) — overview + standalone-vs-umbrella import rule
