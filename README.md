# scitex-types

Scientific type definitions (ArrayLike, ColorLike) and validation utilities.

## Installation

```bash
pip install scitex-types
```

With optional dependencies:

```bash
pip install scitex-types[numpy,pandas]
pip install scitex-types[all]
```

## Usage

```python
from scitex_types import ArrayLike, ColorLike, is_array_like, is_list_of_type

# Type annotations
def process(data: ArrayLike) -> None: ...
def set_color(c: ColorLike) -> None: ...

# Runtime checks
is_array_like([1, 2, 3])           # True
is_list_of_type([1, 2, 3], int)    # True
```
