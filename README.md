# scitex-types

<!-- scitex-badges:start -->
[![PyPI](https://img.shields.io/pypi/v/scitex-types.svg)](https://pypi.org/project/scitex-types/)
[![Python](https://img.shields.io/pypi/pyversions/scitex-types.svg)](https://pypi.org/project/scitex-types/)
[![Tests](https://github.com/ywatanabe1989/scitex-types/actions/workflows/test.yml/badge.svg)](https://github.com/ywatanabe1989/scitex-types/actions/workflows/test.yml)
[![Install Test](https://github.com/ywatanabe1989/scitex-types/actions/workflows/install-test.yml/badge.svg)](https://github.com/ywatanabe1989/scitex-types/actions/workflows/install-test.yml)
[![Coverage](https://codecov.io/gh/ywatanabe1989/scitex-types/graph/badge.svg)](https://codecov.io/gh/ywatanabe1989/scitex-types)
[![Docs](https://readthedocs.org/projects/scitex-types/badge/?version=latest)](https://scitex-types.readthedocs.io/en/latest/)
[![License: AGPL v3](https://img.shields.io/badge/license-AGPL_v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)
<!-- scitex-badges:end -->


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
