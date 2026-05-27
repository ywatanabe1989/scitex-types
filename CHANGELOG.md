# Changelog

All notable changes to `scitex-types` are documented here.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/);
versions follow [Semantic Versioning](https://semver.org/).

## [Unreleased]

## [0.1.6] - 2026-04-30

- ci(docs): make _sphinx_html commit-back step non-fatal
- ci(quality): replace broken ecosystem-clone template with single-package audit-all
- ci(codecov): disable PR comments (comment: false) to stop email noise
- fix(workflows): resync integrated release pipeline from scitex-dev v0.11.20

## [0.1.5] - 2026-04-17

- fix(workflows): standardize to scitex-dev canonical workflow set
- fix(tests): satisfy PA-307 TQ001/TQ002 in cross-package imports test
- deps: collapse fragmented extras into the three-tier policy

## [0.1.4] - 2026-04-09

- docs(readme): PS-167 two-row badge layout
- docs(skills): drop PS-116 banned Interfaces callout from SKILL.md
- ci: normalize workflow filenames + README badges (PS-164)
- quality: NM/TQ cleanup (no-mocks + test-quality migration)
- quality: try_import_optional migration + PA-303 test guards + PS-140 cross-package gate + codecov.yml
- docs(readme): recommend uv pip install
- ci(release): sync publish-pypi.yml fix from ecosystem
- ci: sync GitHub Releases with PyPI publish
- chore(deps): bump scitex-dev pin floor to 0.11.7
- chore(deps): pin scitex-dev>=0.11.5 in [dev] (audit version drift)
- ci(newb): add weekly doc-quality workflow
- docs(readme): add ## Architecture and ## Demo sections (PS141, PS142)
- fix(deps): expand [dev] to include xarray (audit-project PS210)
- docs: add CHANGELOG.md (audit-project PS134/PS135)
- test(audit): integrate audit-all into the test suite, drop audit.yml
- ci(audit): pin scitex-dev to v0.11.1
- ci(audit): add `scitex-dev ecosystem audit-all` workflow
- docs(skills): add mandatory installation/quick-start/python-api leaves
- docs(skills): adopt inline [WHAT]/[WHEN]/[HOW] marker standard
- docs(readme): move badges below Full-Doc line (PS133)
- docs(readme): mark primary interface <details open> (PS131)
- ci: sync-main.yml — auto-FF main on v* tag push
- chore(pyproject): add Documentation URL to [project.urls] (PS127)
- ci+docs: add canonical docs.yml + sphinx/requirements.txt (PS122/PS126)
- docs(readme): include CLI form in 'Part of SciTeX' one-liner (PS120)
- docs(readme): adopt canonical 'Part of SciTeX' one-liner
- audit: clear PS204x2 + PS107/110/112/113 (canonical README + test layout)
- chore(structure): audit-project compliance — tests mirror layout
- fix(release-safety): opt-in publish-pypi.yml (workflow_dispatch only)
- fix(skills): add canonical frontmatter (name, description, tags)
- fix(api): PA501/PA201/PA203 hygiene — `from __future__ import annotations`, `__version__` in `__all__`, fallback `0.0.0+local`
- fix(ArrayLike): include torch.Tensor in the union when torch is installed

## [0.1.3]

- Initial CHANGELOG entry — see git log for prior history.
