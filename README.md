# scitex-types

Scientific type definitions (ArrayLike, ColorLike) and validation utilities.

> **Interfaces:** Python ⭐⭐⭐ (primary) · CLI — · MCP — · Skills ⭐ · Hook — · HTTP —

## Problem and Solution


| # | Problem | Solution |
|---|---------|----------|
| 1 | **`numpy.typing.ArrayLike` covers only NumPy** -- functions that also accept Torch/DataFrame/Series need a hand-rolled `Union` | **`ArrayLike`, `ColorLike`** -- stable aliases spanning `list/tuple/np.ndarray/pd.DataFrame/pd.Series/xr.DataArray/torch.Tensor` + matplotlib color inputs |
| 2 | **Runtime "is this a list of floats?" is a 3-line comprehension** | **`is_array_like()`, `is_list_of_type(lst, float)`** -- clear predicates, no isinstance chain |

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
