---
name: scitex-types
description: |
  [WHAT] Type aliases (`ArrayLike`, `ColorLike`) and runtime type guards (`is_array_like`, `is_list_of_type`/`is_listed_X`) for scientific Python — unions across NumPy/pandas/torch/xarray arrays plus matplotlib color inputs.
  [WHEN] Type-hinting a function that accepts ndarray/DataFrame/Tensor, runtime-checking array-likeness, validating list element types, or typing a matplotlib color parameter.
  [HOW] `from scitex_types import ArrayLike, ColorLike, is_array_like, is_listed_X` — use as type hints or call predicates with values.
tags: [scitex-types]
primary_interface: python
interfaces:
  python: 3
  cli: 0
  mcp: 0
  skills: 1
  http: 0
---

# scitex-types

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

- [01_installation.md](01_installation.md) — pip install + extras + smoke verify
- [02_quick-start.md](02_quick-start.md) — type-hint and runtime-check examples
- [03_python-api.md](03_python-api.md) — all public aliases and predicates
- [10_quick-start.md](10_quick-start.md) — legacy quick-start (kept for context)
- [11_python-api.md](11_python-api.md) — legacy API notes (kept for context)

No CLI, no MCP tools.
