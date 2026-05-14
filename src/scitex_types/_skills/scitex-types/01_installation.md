---
description: |
  [TOPIC] scitex-types Installation
  [DETAILS] pip install scitex-types with optional [numpy], [pandas], [torch], [xarray], [all] extras for runtime predicates against those array libraries.
tags: [scitex-types-installation]
---

# Installation

## Standard

```bash
pip install scitex-types
```

Pure-Python; no required runtime dependencies. The type aliases and
predicates work even when no array library is installed (they just won't
match those types).

## Optional extras

| Extra     | Adds      | Why                                              |
|-----------|-----------|--------------------------------------------------|
| `numpy`   | numpy     | enable `is_array_like(np.ndarray)` matches       |
| `pandas`  | pandas    | enable matches against `DataFrame` / `Series`    |
| `torch`   | torch     | enable matches against `torch.Tensor`            |
| `xarray`  | xarray    | enable matches against `xarray.DataArray`        |
| `all`     | all above |                                                  |

```bash
pip install 'scitex-types[numpy,pandas]'
pip install 'scitex-types[all]'
```

## Verify

```bash
python -c "import scitex_types; print(scitex_types.__version__)"
python -c "from scitex_types import ArrayLike, ColorLike, is_array_like; print('ok')"
```

## Editable install (development)

```bash
git clone https://github.com/ywatanabe1989/scitex-types
cd scitex-types
pip install -e '.[dev]'
```

## Umbrella alternative

```bash
pip install scitex   # exposes scitex.types as a submodule
```

See SKILL.md for the standalone-vs-umbrella import rule.
