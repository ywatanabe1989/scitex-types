# scitex-types

<p align="center">
  <a href="https://scitex.ai">
    <img src="docs/scitex-logo-blue-cropped.png" alt="SciTeX" width="400">
  </a>
</p>

<p align="center"><b>Scientific type aliases (ArrayLike, ColorLike) + runtime validation predicates.</b></p>

<p align="center">
  <a href="https://scitex-types.readthedocs.io/">Full Documentation</a> · <code>pip install scitex-types</code>
</p>

<!-- scitex-badges:start -->
<p align="center">
  <a href="https://pypi.org/project/scitex-types/"><img src="https://img.shields.io/pypi/v/scitex-types.svg" alt="PyPI"></a>
  <a href="https://pypi.org/project/scitex-types/"><img src="https://img.shields.io/pypi/pyversions/scitex-types.svg" alt="Python"></a>
  <a href="https://github.com/ywatanabe1989/scitex-types/actions/workflows/test.yml"><img src="https://github.com/ywatanabe1989/scitex-types/actions/workflows/test.yml/badge.svg" alt="Tests"></a>
  <a href="https://github.com/ywatanabe1989/scitex-types/actions/workflows/install-test.yml"><img src="https://github.com/ywatanabe1989/scitex-types/actions/workflows/install-test.yml/badge.svg" alt="Install Test"></a>
  <a href="https://codecov.io/gh/ywatanabe1989/scitex-types"><img src="https://codecov.io/gh/ywatanabe1989/scitex-types/graph/badge.svg" alt="Coverage"></a>
  <a href="https://scitex-types.readthedocs.io/en/latest/"><img src="https://readthedocs.org/projects/scitex-types/badge/?version=latest" alt="Docs"></a>
  <a href="https://www.gnu.org/licenses/agpl-3.0"><img src="https://img.shields.io/badge/license-AGPL_v3-blue.svg" alt="License: AGPL v3"></a>
</p>
<!-- scitex-badges:end -->

---

## Problem and Solution

| # | Problem | Solution |
|---|---------|----------|
| 1 | **`numpy.typing.ArrayLike` covers only NumPy** — functions that also accept Torch/DataFrame/Series need a hand-rolled `Union` | **`ArrayLike`, `ColorLike`** — stable aliases spanning `list/tuple/np.ndarray/pd.DataFrame/pd.Series/xr.DataArray/torch.Tensor` + matplotlib color inputs |
| 2 | **Runtime "is this a list of floats?" is a 3-line comprehension** | **`is_array_like()`, `is_list_of_type(lst, float)`** — clear predicates, no isinstance chain |

## Installation

```bash
pip install scitex-types
# Optional extras:
pip install scitex-types[numpy,pandas]
pip install scitex-types[all]
```

## Quick Start

```python
from scitex_types import ArrayLike, is_array_like, is_list_of_type

def process(data: ArrayLike) -> None: ...

is_array_like([1, 2, 3])           # True
is_list_of_type([1, 2, 3], int)    # True
```

## 1 Interfaces

<details open>
<summary><strong>Python API</strong></summary>

<br>

```python
from scitex_types import ArrayLike, ColorLike, is_array_like, is_list_of_type

# Type annotations
def process(data: ArrayLike) -> None: ...
def set_color(c: ColorLike) -> None: ...

# Runtime checks
is_array_like([1, 2, 3])           # True
is_array_like("not array")         # False
is_list_of_type([1, 2, 3], int)    # True
is_list_of_type([1, "x"], int)     # False
```

</details>

## Part of SciTeX

`scitex-types` is part of [**SciTeX**](https://scitex.ai). Install via
the umbrella with `pip install scitex[types]` to use as
`scitex.types` (Python) or `scitex types ...` (CLI).

>Four Freedoms for Research
>
>0. The freedom to **run** your research anywhere — your machine, your terms.
>1. The freedom to **study** how every step works — from raw data to final manuscript.
>2. The freedom to **redistribute** your workflows, not just your papers.
>3. The freedom to **modify** any module and share improvements with the community.
>
>AGPL-3.0 — because we believe research infrastructure deserves the same freedoms as the software it runs on.

## License

AGPL-3.0-only (see [LICENSE](./LICENSE)).

---

<p align="center">
  <a href="https://scitex.ai" target="_blank"><img src="docs/scitex-icon-navy-inverted.png" alt="SciTeX" width="40"/></a>
</p>
