# Changelog

All notable changes to `scitex-types` are documented here.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/);
versions follow [Semantic Versioning](https://semver.org/).

## [Unreleased]

## [0.2.0]

- feat: port `var_info` from `scitex_gen._var_info` (Phase B of the
  scitex-gen full retirement wave). New public symbol. The port uses
  `scitex_dev.try_import_optional` so the array-shape branch degrades
  gracefully when numpy / pandas / xarray / torch is absent (matches
  the `ArrayLike` policy already in place here).
- Note on `ArrayLike`: NOT re-imported from scitex-gen. The
  `scitex_types.ArrayLike` shipping here is strictly more capable
  (lazy / optional-dep aware), and the scitex_gen variant will be
  dropped in the scitex_gen retirement PR.

## [0.1.3]

- Initial CHANGELOG entry — see git log for prior history.
