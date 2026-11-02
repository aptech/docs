# Containerized GAUSS app-help build

Date: 2026-10-26
Status: Implemented and validated. Offline end-to-end builds, application-version
Qt consumer checks, repeatability and 2 GiB resource test passed. See final handoff.

Follow-up complete: user found the installed help stops at 26.1.4. That was the
pinned archive's content, not an installation/cache error. Rebuilt from published
qthelp `f7b290e34a849af3d1670ad52d0c521e54ec0090` with explicit release 27;
no master/develop merge is needed. New release validation rejects mismatched
source changelogs and mismatched generated changelog/welcome/Sphinx versions.
Local qthelp has eight unpublished commits, remote has thirteen unique commits;
neither source branch nor dirty files are modified. Published origin/qthelp is
the chosen input. The new bundle is `inputs-27/` and build `run27-01/` on the
same Alma9 validation host. All checks passed, including Qt 5.15.8/5.15.19 and
rendered changelog 27.0.0. Installed in `~/gauss27-arm/help` with backup
`.backup-app-help-20261026-193041/`. Actual installed QCH first changelog section
verified as 27.0.0. Runtime 204.39 s / peak 1.17 GiB under a 2 GiB limit.
Evidence: `app-help/evidence/gauss27/`; local output: `app-help/artifacts/gauss27/`.
NEXT: User restarts GAUSS to reload help. BLOCKER: none.

Styling follow-up: user supplied blue minimize and gray tsAggregate screenshots.
Both current packaged pages use the same markup/styles; the intended gray CSS
was converted to website `.bd-content` selectors in `b79b5aa3`, while app help
renders `.rst-content`. Added scoped `app-help/app-help.css` to restore the
previous gray signature palette, borders/padding and parameter heading border
behavior. Content inputs remain published qthelp f7b290e / release 27. Build
`run27-style` passed; Qt previews of both reported pages show matching gray boxes
and 12px padding. Comparing every QCH resource hash found only
`theme_override.css` changed. Final build `run27-style-final` extends the same
scope to all GAUSS definitions (including the existing data definitions).
Final build passed all checks and Qt 5.15.8/5.15.19 screenshots were inspected.
Installed and hash-verified in `~/gauss27-arm/help`, with backup
`.backup-app-help-20261026-195133/`. Evidence is in
`app-help/evidence/gauss27-style/`; local artifacts in
`app-help/artifacts/gauss27-style/`. NEXT: Restart GAUSS. BLOCKER: none.

## Objective and scope

Produce the application help files `gauss.qch` and `gauss.qhc` in a disposable
Linux container, runnable on the existing Linux build VM and later callable by
the application build. Prefer this over a dedicated always-on VM or Lambda.
Deliver the implementation and validation, not another planning-only report.
Preserve the current help content and application compatibility first.

Do not modify the production aliases, publish website docs, replace installed
application help, commit generated help to SVN, or enable a production pipeline.
Those actions are outside this implementation. A repeatable local build command
and a concrete integration example are in scope. No new VM is required.

## Established facts

- Source workspace: `/Users/jason/svn/gxmldoc`, branch `qthelp`, remote
  `git@github.com:aptech/docs.git`. It has unrelated tracked and untracked changes.
  Work in a separate Orca worktree; do not reset or copy unrelated edits.
- Untracked reference copies exist at `builddoc.sh` and `mkhelp.sh` in that
  workspace. Read them there; a fresh checkout will not contain them.
- On `root@apt`, the aliases are:
  - `buildg`: `/root/bin/builddoc.sh main/gauss` (master checkout, website staging).
  - `builddevg`: `/root/bin/builddoc.sh develop/gauss develop`.
  - `buildarchiveg`: `/root/bin/builddoc.sh archive/gauss archive build.qthelp`.
  - `deployg`: `/root/bin/deploydoc.sh gauss` (staging to production).
- `buildarchiveg` runs **make html**, not the Sphinx qthelp builder. It pulls the
  archive checkout, updates submodules with `--remote` except the theme, builds
  HTML, rewrites some links, then copies into the webroot. Its root requirement
  comes from orchestration/publishing, not a demonstrated Sphinx requirement.
- Archive sources: `/home/readthedocs/source/docs/archive/gauss`, branch `qthelp`.
  Inspected HEAD: `7c9e3736fd4c7e557b69e2e6c0c127efc528b69f`.
- Build environment: `/home/readthedocs/build.qthelp`, Python 3.8.5 in `venv`,
  Sphinx 3.4.3, installed sphinx-rtd-theme 0.5.2, sphinx-design 0.0.13,
  sphinx-panels 0.4.1, sphinx-tabs 3.4.1. The requirements file has many unrelated
  packages and omits installed sphinx-design. Do not blindly copy it as a lock.
- Server archive `docs/conf.py` uses sphinx_design. `conf_qthelp.py` is present
  but the inspected command does not select it. Repository requirements currently
  specify Sphinx 7.4.7; that is not the archive server environment.
- Server theme submodule checkout is `d64dadf1ceec4f9ff6c1ca2d3ea4c3d0fdb0e8d2`,
  whereas the parent records `6909b4acb2319330532fd449d72d0879c39b3813`.
  Theme working files were clean. Verify which theme files Sphinx actually loads.
  Archive checkout also has untracked static files and tspdlib; assess relevance.
- Existing archive HTML occupies about 98 MB. This is not a memory measurement.
- The local reference `mkhelp.sh` downloads `apt:~/docs.aptech.com/archive/*`,
  merges legacy `HTML5`, welcome pages, fonts, and MathJax, flattens and rewrites
  assets, invokes `clean_sphinx.py`, `genhelpproperties.py`, and `help.py`, then
  Qt `qcollectiongenerator` with `gauss.qhcp`. It outputs gauss.qch/gauss.qhc.
  It hardcodes a `/home/jason/svn/21/x64/html5docsync.new/qt` toolchain and ends
  with an SVN update/copy/commit. Do not execute it unmodified.
- Sphinx runs four workers and the reference cleanup launches fourteen Python
  jobs. Peak memory and runtime are unknown. Start validation with 4 GB available;
  measure before promising that 1 GB is sufficient.

## Implementation sequence

1. Resolve the inputs and execution host. Locate the complete packaging checkout
   (HTML5, etc, three Python scripts, gauss.qhcp and Qt tools), its actual current
   source-control owner, and its applicable instructions. The local script may
   be stale. Inspect available machine configuration and read-only remote state
   before asking Jason for missing paths. Do not assume SVN-era paths are current.
   The user suggested the Linux build VM on Palladio. Local SSH configuration
   also says Hermes moved to Janus and defines hermes-janus and alma9-janus;
   confirm the intended active Linux builder and available Docker/Podman runtime.
   If ambiguous, ask one focused question and continue independent local work.
2. Record the effective known-working dependency versions, relevant source and
   submodule revisions, required legacy assets, and Qt compatibility requirements.
   Capture enough information to reconstruct the build without apt. Use apt only
   for read-only discovery/baseline retrieval. Do not run its publishing scripts.
3. Implement a Dockerfile/container recipe, pinned dependency manifest, and a
   single documented build entrypoint with explicit inputs and output directory.
   Keep source read-only where practical, use isolated scratch/output locations,
   avoid host-specific paths and credentials in images, and expose concurrency.
   Resolve source revisions outside the build; no git pull or moving submodules
   during artifact generation. Acquire any external CSS/fonts/MathJax at a pinned
   preparation stage so artifact generation can run without network access.
4. Build archive HTML locally, preserving required link fixes, and feed it directly
   into an adapted help packager. Retain navigation, keywords, namespaces, and
   collection settings. Do not replace the custom pipeline with generic Sphinx
   qthelp output without establishing equivalence. Fail on missing required inputs
   and failed subprocesses; remove automatic publishing and SVN commits from the
   new entrypoint. Keep existing website builds unchanged.
5. Validate end to end on Linux. Produce both help files; inspect Qt/database
   integrity, expected namespace, TOC, keywords and referenced resources. Compare
   representative content against the existing help baseline, including command
   reference, legacy user guide, images, math, and internal links. Exercise search
   and rendering in a compatible Qt help consumer/application if available; report
   any unavailable GUI validation explicitly. Check generation without network
   after preparation. Run twice and explain any expected metadata differences.
6. Measure whole-container peak memory and elapsed time, not just one child
   process. Start with bounded concurrency and 4 GB; lower limits only when useful
   and report measured outcomes. Do not impose a 1 GB requirement.
7. Deliver the recipe, command, source/dependency provenance, validation results,
   measured resource recommendation, and application-build integration example.
   Save exact continuation/blockers in this plan. Do not claim completion based
   only on Dockerfile syntax or HTML output; the deliverable is usable app help.

## Implementation checkpoint (2026-10-26)

- Owner: `term_09cf6175-de7e-4f0b-901f-6231752ba500`.
- Recipe: `app-help/` in this worktree, based on master `d395f462`; documentation
  input is separately pinned to archive qthelp `7c9e3736fd4c7e557b69e2e6c0c127efc528b69f`.
  Local qthelp `2cb15a6` and origin/qthelp `f7b290e` are different and were not
  silently substituted. No source workspace changes were copied.
- Active builder: `alma9-janus`, AlmaLinux 9.7, Podman 5.6.0, cgroup v2, 8 GB VM.
  Hermes has no Docker/Podman. Work is isolated under
  `/home/jason/work/app-help-container-20261026`.
- Packaging owner: Janus `/home/jason/svn/21/x64/html5docsync.new`, SVN
  `svn+ssh://svnext/data/rep/guiroot/helpgen/trunk`, revision 6942 (last changed 6925).
  HTML5, gauss.qhcp, generated baseline are untracked; welcome and mkhelp.sh modified.
  Required inputs were copied read-only and SHA256 sealed, including these files.
- Installed `sphinx-rtd-theme==0.5.2` is effective: Sphinx searches
  `_themes/<name>/theme.conf`, while the checkout has another nested
  `sphinx_rtd_theme/` directory. Server source and `find_themes` code verified.
- No applicable filesystem AGENTS.md found along worktree/packager ancestor paths.
  User-provided communication/handoff instructions apply.
- First image built from a digest-pinned Python 3.10.16 image, Debian 20250301
  snapshot and hash-locked Python closure. Qt generator/consumer 5.15.8; actual
  application Qt 5.15.19 available on Alma9 and Janus for additional checks.
- Run01: rootless VM does not delegate CPU controller; removed optional CPU quota,
  retained worker cap, pids cap, network isolation and 4 GB memory limit. No VM
  configuration changed.
- Run02/03: Sphinx fails on unresolved sphinx-design stretched links. Restored
  archive docutils 0.18.1 (despite Sphinx's stale declared upper bound), then
  traced the actual failure to the missing untracked tspdlib source tree.
  Confirmed it is clean Git at `ed4199d0a6821604940a108aa4664813ae551843` and
  added its immutable archive to inputs; applications.rst requires its card target.
- Run04 is the next offline artifact test. Scripts retain custom properties,
  namespace `com.aptech.gauss.25.0`, identifiers and QHCP settings. Full MathJax 2.7.9
  fixes the old loader-only packaging gap. All build inputs mount read-only;
  output/scratch isolated; no SVN/publishing/apt-server calls during generation.
- `memory.peak` is available inside the container cgroup (although absent at the
  host root cgroup). Runner records the kernel whole-cgroup peak, memory events,
  elapsed time and an independent 20 ms sample series maximum.

## Final handoff (2026-10-26)

- Implementation: `app-help/README.md` gives image/input preparation, one-command
  generation and application pipeline staging. `app-help/VALIDATION.md` records
  acceptance evidence and limitations. `app-help/evidence/` is the compact durable
  record, including all 6,089 input hashes and exact delivered artifact hashes.
- Delivered local files: `app-help/artifacts/validated/gauss.qch` and `gauss.qhc`
  (ignored by Git). Complete logs/reports/screenshots alongside; native Qt evidence
  in `app-help/artifacts/native/`.
- Durable Linux directory: `alma9-janus:/home/jason/work/app-help-container-20261026`.
  `inputs/` is the sealed bundle; `recipe/` the runnable implementation; `run06/`
  the delivered output; `run07/` the repeat with a 2 GiB limit.
- Final image ID: `e3635d72e287911df7470aa76e16138491700d85eb7b10f71337a1a88ff0a8bb`.
- Run05 passed (205 s, 1.16 GiB peak). Final recipe run06 passed (199.10 s,
  1.17 GiB peak, 4 GiB limit). Same-image run07 passed (197.86 s, 1.05 GiB peak,
  2 GiB limit). All measurements are kernel whole-cgroup peaks, with zero OOMs.
  Recommend two workers / 2 GiB; leave default at 4 GiB. Do not promise 1 GiB.
- Qt 5.15.8 and application Qt 5.15.19 passed search (41 regression results), OLS
  context lookup, different-namespace application home resolution, rendering of
  welcome/reference/legacy guide, MathJax and both plotxy images. Five screenshots
  inspected. The full GAUSS executable was not launched; no installed help changed.
- 5,728 resources, 1,736 TOC entries, 1,735 keywords; all TOC targets valid.
  Representative text and plot image match baseline. No new missing links/anchors.
  Existing 130 broken file references / 2 anchor defects remain explicitly recorded.
- Legacy missing MathJax tree and incorrect GG.8 TOC target corrected in staged
  output only. No source, production alias, webroot, publishing or SVN changes.
- Repeated builds have identical logical QCH/QHC content. Binary differences are
  SQLite physical layout, Qt filter-ID order and collection timestamps; comparison
  normalizes only those items and preserves all content/filter relationships.
- NEXT: Review the implementation and use the documented staging example when
  intentionally wiring an application build. No further implementation input needed.
- BLOCKER: none.

## Acceptance and reporting

- One documented command produces both files into a caller-selected directory
  from explicit inputs, without apt access, publishing, or source-control writes.
- Required assets and scripts have identified owners and reproducible provenance.
- Generated help passes the structural/content checks; GUI compatibility results
  and any limitations are stated, with actual memory/time measurements.
- Unrelated workspace edits and production services remain untouched.
- At each meaningful checkpoint, report your Orca handle and a short HANDOFF:
  OBJECTIVE, DONE, CURRENT, NEXT, BLOCKER. Use concise, simple language.
- The launching session is transferring ownership, not supervising you. Proceed
  autonomously with implementation and testing; ask only for unresolved inputs or
  permissions that actually block progress. Update your Orca workspace comment.

## Beta rebuild (2026-11-02, app-help-container-0e)

- Trial from published qthelp 63f9762d passed on alma9-janus (205.7 s, 1.05 GiB peak, 2 GiB cap). Only
  changelog, gmmfit, gmmfitiv and searchindex.js differ from the 259bae2e build; counts unchanged.
- Builder script `final-build-20261102.sh <sha> <tag>` prepares from published qthelp only, builds, runs the
  app-Qt probe (`probe-20261102/src/help_probe`, adapted from q30r-01) and diffs against the trial. A dry run
  reproduced the trial QCH byte for byte.
- Final build waits on GMM commit B docs and a GDAT decision. Report: ~/orca/pillars/reports/help-rebuild-beta.md.
- Final: docs qthelp 6b3db60f (GDAT 5c45a5fb + 0f237eab, GMM B 6b3db60f). qtgui commit 4d8570f8 on
  `jason-d-jones/help-rebuild-beta` (parent 5a3d3800), qch 93d98f91, qhc 65290428. Built pre-push from a bundle in
  the builder clone (`ALLOW_UNPUBLISHED=1`), then confirmed the published head is the same SHA.
- Content audit after 4d8570f8: fixed docs (qthelp 4461374c) and packaging (cc/ and coming-to-gauss/ pages,
  unshipped links as text, straight quotes). qtgui 63f5ed5f. Image beta-20261102 a54f581e. Always scan the
  page text (competitors, internal paths, "unreleased", raw markup) and view new screenshots before shipping.
