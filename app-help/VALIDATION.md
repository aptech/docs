# Validation record — 2026-10-26

## App-help styling correction (latest installed build)

Restored the gray signature boxes shown in the user's reference. The website
stylesheet switched its override to `.bd-content` in `b79b5aa3`; Qt help uses
`.rst-content`, so it fell back to RTD's blue boxes. `app-help.css` now applies
the previous palette, padding and parameter-header border behavior to GAUSS
definitions using the actual app container and literal colors.

- Qt 5.15.8 computed styles on both minimize and tsAggregate: background
  `rgb(248,248,248)`, text/top border `rgb(69,85,96)`, top border 3px, padding
  12px, function name `rgb(0,85,127)`. Screenshots inspected in Qt 5.15.8 and
  application Qt 5.15.19. Both pages now use the gray style.
- All checks passed; 204.84 s, kernel peak 1,267,044,352 bytes, 2 GiB cap.
- Compared every embedded resource with the preceding GAUSS 27 build:
  **only `theme_override.css` changed**. Content and release remain unchanged.
- Installed in `~/gauss27-arm/help` and verified both hashes. Backup:
  `.backup-app-help-20261026-195133/`. Restart GAUSS to reload the collection.
- Local output: `app-help/artifacts/gauss27-style/`; native screenshots:
  `app-help/artifacts/native27-style/`; evidence: `app-help/evidence/gauss27-style/`.
- Linux output: `run27-style-final/`; same sealed `inputs-27/`. The current
  image ID is recorded in `evidence/gauss27-style/image-id.txt`.

## GAUSS 27 content correction

The original validated archive replay stopped at **26.1.4**. Installing that pair
in GAUSS 27 did not make its content current. The user caught this; the source pin
was the cause, not a failed copy or a need to merge master/develop.

Rebuilt from published `origin/qthelp`
`f7b290e34a849af3d1670ad52d0c521e54ec0090` (118 commits after the archive) with
explicit release **27**. Local qthelp has eight unpublished commits and the remote
has thirteen unique commits; this build uses the published revision and includes
no dirty files or local-only commits. No source branches were merged or changed.

- Latest changelog **27.0.0**, welcome **GAUSS 27**, Sphinx release **27** verified
  from the actual QCH. Preparation and validation now reject release mismatches.
- Two negative checks reject the old archive source/artifact when 27 is requested.
- Offline build passed in **204.39 s**, kernel cgroup peak **1,260,621,824 bytes**
  (1.17 GiB), 2 GiB limit, no OOMs.
- 5,733 resources, 1,742 TOC entries, 1,741 keywords; no new missing local links.
- Qt 5.15.8 and 5.15.19 passed; changelog added to rendering checks. Screenshot
  inspected: 27.0.0 appears first. GAUSS 27's home URL resolves correctly.
- Installed both files in `/Users/jason/gauss27-arm/help`; verified both hashes
  and read the installed changelog directly. Backup:
  `help/.backup-app-help-20261026-193041/`. Restart GAUSS to reload an open engine.
- Local artifacts: `app-help/artifacts/gauss27/`; native screenshots in
  `app-help/artifacts/native27/`; durable evidence in `app-help/evidence/gauss27/`.
- Linux inputs/output: the existing isolated work directory's `inputs-27/` and
  `run27-01/`. Image ID:
  `c10700d882c836f7bde9196e372763b7ae5bfcb6594f8892403102234048ea1e`.

The remaining sections record the original archive-baseline validation, not the
current installed content. Its artifacts and evidence remain available unchanged.

Implementation and tests ran in this independent docs worktree and in
`alma9-janus:/home/jason/work/app-help-container-20261026`. Production aliases,
webroots, installed GAUSS help, original packaging files and SVN were not changed.

## Delivered artifacts

Local, excluded from Git:

- `app-help/artifacts/validated/gauss.qch`
- `app-help/artifacts/validated/gauss.qhc`
- `app-help/artifacts/validated/`: complete generation log, input/dependency locks,
  resource measurements, content audit and Qt 5.15.8 screenshots.
- `app-help/artifacts/native/`: Qt 5.15.19 results and inspected screenshots.

Durable Linux copies: `alma9-janus:/home/jason/work/app-help-container-20261026/run06`.
Inputs: the sibling `inputs/` directory, sealed by `evidence/inputs.lock.json`.
Recipe: the sibling `recipe/` directory. All paths are outside production.

Validated image ID (amd64; approximately 778 MB uncompressed):

```text
e3635d72e287911df7470aa76e16138491700d85eb7b10f71337a1a88ff0a8bb
```

One command on that VM, using a new output directory:

```sh
/home/jason/work/app-help-container-20261026/recipe/build.sh \
  --inputs /home/jason/work/app-help-container-20261026/inputs \
  --output /home/jason/work/app-help-container-20261026/my-build \
  --image e3635d72e287911df7470aa76e16138491700d85eb7b10f71337a1a88ff0a8bb
```

The exact delivered QCH/QHC SHA256 values are in
`evidence/artifacts.sha256.json`. Qt-native validation records its input QCH
hash, which matches the delivered QCH.

## Actual output checks

- SQLite integrity checks passed for both files; every stored resource
  decompressed to its declared length.
- 5,728 packaged resources, 1,736 TOC entries and 1,735 keywords. Baseline keyword
  count is also 1,735. Every TOC target exists, including the corrected old
  `GG.8-InteractingwithPlots` → `GG.8.0-InteractingwithPlots` reference.
- Namespace preserved: `com.aptech.gauss.25.0`; collection registers adjacent
  `gauss.qch` with no build-host path. QHCP settings and custom filters retained.
- Welcome, legacy index/introduction, command reference, OLS and normal CDF pages
  have the same visible text as the baseline. The representative plot image is
  byte-identical. Content was checked from the compressed database, not just HTML.
- No new missing local file references, anchor targets or external resources
  compared with the baseline. Full inventories are in the validation JSON.
- Complete offline MathJax 2.7.9 loader, configuration, fonts and extensions are
  included. Its tests/examples are excluded from application help.
- The prepared Git/export/download bundle exactly matched all **6,089** file
  hashes in the independently captured source snapshot. Preparation no longer
  depends on the archive server.
- Tampered inputs failed before container launch. Nonempty output directories
  failed without modifying their contents. Read-only input verification passed
  after builds. Subprocess failures propagated to a nonzero build exit status.

## Qt consumer checks

Both Qt 5.15.8 (inside the offline container) and the application's installed Qt
5.15.19 opened relocated disposable copies, rebuilt search, found **41** results
for `regression`, resolved the `ols` context identifier, and rendered five pages:
welcome, OLS, normal CDF, legacy introduction and plotxy.

MathJax produced 9 math elements on OLS and 6 on the CDF page. Both plot images
loaded. The Qt 5.15.8 probe recorded **zero failed resource requests**. Screenshots
were visually inspected for readable text, layout, icons, code and plots.

Qt successfully resolves the application's home URL with its different namespace
(`qthelp://aptech.com.gauss.26.0/doc/welcome.html`) to the preserved namespace.

These are actual offscreen Qt Help/WebKit consumers, including one linked to the
application's Qt libraries. The full installed GAUSS executable was **not**
launched or modified. Windows/macOS application UI testing is not claimed. The
native Qt install logs an OpenSSL 1.x/3.x mismatch; all help access is through
the local help-engine adapter, and the tested operations succeed without TLS.

## Resources and repeatability

All generation runs use `--network=none`, a read-only root/input mount, no swap
above the memory limit, and two Sphinx/cleanup workers. Resource measurements cover
the **whole cgroup**, including all child processes, file cache, Qt indexing and
rendering. Kernel `memory.peak` is used; `memory.events` showed no OOM kills.

| Run | Limit | Elapsed | Kernel peak | Result |
|---|---:|---:|---:|---|
| run05 | 4 GiB | 204.95 s | 1,244,868,608 bytes (1.16 GiB) | Passed |
| run06 (delivered) | 4 GiB | 199.10 s | 1,258,483,712 bytes (1.17 GiB) | Passed |
| run07 (same image, repeat) | 2 GiB | 197.86 s | 1,123,495,936 bytes (1.05 GiB) | Passed |

**Recommendation: two workers and a 2 GiB container limit** on the existing VM.
The default remains the requested conservative 4 GiB; pass `--memory 2g` for the
tested smaller allocation. Budget about four minutes per build plus image/input
preparation. A 1 GiB limit is not recommended from these measurements. Allow
roughly 1 GB for the image, 1 GB scratch space and 100 MB per retained output.

`compare.py` compares all logical database tables. Repeated output has identical
help content, indexes, TOC, resources, filters and collection settings. Byte hashes
differ because SQLite storage layout is not canonical, Qt assigns filter IDs
through a hash set, and the collection records creation/registration/QCH-file
timestamps. Comparison normalizes only those timestamps and filter IDs (including
their relationships); it does not ignore content tables.

## Preserved limitations and deliberate differences

- **130 inherited missing file references and 2 inherited missing anchors remain.**
  Examples include old user-guide names, omitted nested website category pages,
  and malformed image paths in source RST. These also fail in the existing help
  baseline. The container migration does not silently rewrite their content.
- Sphinx reports 1,631 source warnings, including existing ambiguous references,
  theme-demo RST and missing image-size information. The build does not use `-W`;
  actual output checks enforce the relevant packaging contract.
- The old package included 102 `.bak`/`.new` backup files. They are excluded, as
  are the unused untracked g25 stylesheet and the externally downloaded standalone
  Font Awesome CSS. Required icons/fonts render using the packaged styles.
- Fourteen basename collisions follow a deterministic equivalent of the legacy
  copy precedence; each is recorded in `generation.json`. Source and baseline
  visual/content checks cover the retained custom layout.
- Python/Jinja/MarkupSafe differ from the old archive runtime as listed in README;
  Sphinx, sphinx-design, docutils and effective theme versions match it.
- No publishing, automatic SVN commit, production pipeline enablement, or
  installed-help replacement was performed.
