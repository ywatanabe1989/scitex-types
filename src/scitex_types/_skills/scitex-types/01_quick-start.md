<!-- 01_quick-start.md -->

# scitex-types — Quick Start

## Install

```bash
pip install scitex-types
```

## Import

```python
from scitex_types import ArrayLike, ColorLike, is_array_like, is_listed_X
```

## Usage

### Type-hint an array-like argument

```python
from scitex_types import ArrayLike

def normalize(x: ArrayLike) -> ArrayLike:
    ...
```

### Runtime check for array-likeness

```python
from scitex_types import is_array_like

is_array_like([1, 2, 3])          # True
is_array_like("hello")            # False
```

### Check a list is homogeneous

```python
from scitex_types import is_listed_X

is_listed_X([1, 2, 3], int)       # True
is_listed_X([1, "2"], int)        # False
```
