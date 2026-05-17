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

Per the ecosystem-wide three-tier dependency policy, scitex-types
exposes a single fully-featured extra plus a maintainer-only `dev`
extra. Fragmented `[numpy] [pandas] [torch] [xarray]` extras were
collapsed into `[all]` — install the full matrix in one go.

| Extra   | Adds                                | Why                                                                                       |
|---------|-------------------------------------|-------------------------------------------------------------------------------------------|
| `all`   | numpy + pandas + torch + xarray     | widen `ArrayLike`, enable `is_array_like()` matches against every supported array library |
| `dev`   | pytest, pytest-cov, sphinx toolchain| maintainer-only — tests + docs build                                                      |

```bash
pip install 'scitex-types[all]'           # consumer: full feature set
pip install -e '.[all,dev]'               # maintainer: tests + docs + arrays
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
