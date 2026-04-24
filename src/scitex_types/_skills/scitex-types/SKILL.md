---
name: scitex-types
description: Type aliases and runtime type guards for scientific Python — unions across NumPy/pandas/torch arrays, matplotlib color inputs, and list-of-T predicates. Public API (5 symbols) — `ArrayLike` (union alias spanning `list`, `tuple`, `np.ndarray`, `pd.DataFrame`, `pd.Series`, `xr.DataArray`, `torch.Tensor` for type hints), `ColorLike` (union alias for matplotlib-compatible color inputs — RGB tuples, hex strings, named colors), `is_array_like(obj)` (runtime predicate for array-ish inputs), `is_list_of_type(obj, T)` (runtime check that every element is of type T), `is_listed_X(obj, X)` (alias for is_list_of_type). No CLI, no MCP tools. Drop-in replacement for `numpy.typing.ArrayLike` (narrower — NumPy only), `typing.Union[np.ndarray, torch.Tensor, pd.DataFrame, ...]` hand-rolled unions, `isinstance(x, (list, np.ndarray, ...))` chains scattered across code, and `all(isinstance(el, T) for el in lst)` one-liners. Use whenever the user asks to "type-hint a function that accepts ndarray/DataFrame/Tensor", "check at runtime whether something is array-like", "validate that a list contains only floats/ints/strings", "type a matplotlib color parameter", or mentions `ArrayLike`, `ColorLike`, `scitex.types`, duck-typing array inputs.
user-invocable: false
primary_interface: python
interfaces:
  python: 3
  cli: 0
  mcp: 0
  skills: 1
  hook: 0
  http: 0
---

# scitex-types

> **Interfaces:** Python ⭐⭐⭐ (primary) · CLI — · MCP — · Skills ⭐ · Hook — · HTTP —

Small type-support package for the SciTeX ecosystem. Provides array-ish and
color-ish type aliases plus runtime predicates to check container uniformity.

## Installation & import (two equivalent paths)

The same module is reachable via two install paths. Both forms work at
runtime; which one a user has depends on their install choice.

```python
# Standalone — pip install scitex-types
import scitex_types
scitex_types.ArrayLike(...)

# Umbrella — pip install scitex
import scitex.types
scitex.types.ArrayLike(...)
```

`pip install scitex-types` alone does NOT expose the `scitex` namespace;
`import scitex.types` raises `ModuleNotFoundError`. To use the
`scitex.types` form, also `pip install scitex`.

See [../../general/02_interface-python-api.md] for the ecosystem-wide
rule and empirical verification table.

## Sub-skills

- [01_quick-start.md](01_quick-start.md) — install, import, three usage snippets
- [02_python-api.md](02_python-api.md) — all public aliases and predicates

No CLI, no MCP tools.
