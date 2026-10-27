# GAUSS application help container

Builds the custom GAUSS application help (`gauss.qch` and `gauss.qhc`), including
the legacy user guide, command identifiers and navigation. This does **not** use
Sphinx's generic qthelp builder or run the website publishing scripts.

`app-help.css` restores the gray function-signature boxes, padding and parameter
header borders used before the website stylesheet moved to `.bd-content`.
The app's RTD template uses `.rst-content`, so website-only selectors do not
apply there. This scoped stylesheet is appended during packaging; source docs
and website builds are unchanged. Qt previews include minimize and tsAggregate.

**GAUSS 27:** use documentation commit
`f7b290e34a849af3d1670ad52d0c521e54ec0090` from published `qthelp`, and pass
`--release 27` to `prepare.py`. The original archive replay below ends at 26.1.4;
it establishes packaging compatibility, not current GAUSS 27 content. A newer
application executable does not update the content inside its help files.

## Build from prepared inputs

On a Linux machine with Podman (tested) or Docker and Python 3:

```sh
./app-help/build.sh --inputs /absolute/path/inputs-27 --output /absolute/path/new-output
```

The output directory must be empty. Default concurrency is 2, memory limit 4 GB.
Options: `--jobs 1..16`, `--memory 4g`, `--runtime podman|docker`, `--image IMAGE`.
Prepare the image first; the build resolves it to a local immutable image ID and
uses `--pull=never`. The wrapper disables networking, mounts inputs read-only,
runs as the caller, drops capabilities, makes the image read-only and deletes its
private scratch directory. It neither updates source control nor publishes.

Success requires artifact, content and Qt consumer checks. On failure the command
returns nonzero and keeps logs/partial output for diagnosis; never consume a
failed build's help files. Each successful output also includes checksums and
input provenance, dependency manifests, validation JSON, screenshots and measured
whole-container memory/runtime. The QCH and QHC must remain adjacent.

## Prepare the image (network permitted here)

```sh
podman build -t localhost/gauss-app-help:validation ./app-help
```

The base Python 3.10.16 image is pinned by SHA256 digest. Native packages resolve
against the fixed Debian **20250301T000000Z** snapshot, and the complete Python
closure is version/hash locked. This stage uses Debian apt, but never accesses
the production host named `apt`. Artifact generation uses neither package
installation nor network access. Preserve/export the resulting image by ID in
your artifact store for builds that must also prepare offline.

Sphinx 3.4.3, sphinx-design 0.0.13 and the effective theme 0.5.2 match the archive.
The archive uses docutils 0.18.1 beyond Sphinx's declared upper bound; the explicit
closure intentionally uses `--no-deps` to reproduce that working combination.
Python is upgraded from 3.8.5 to 3.10.16, Jinja2 from 2.11.2 to 3.0.3, and
MarkupSafe from 1.1.1 to 2.1.5. These changes are covered by actual output checks.
The image records installed native and Python versions in every build output.

## Prepare explicit source inputs

The recipe checkout's branch is **not** the documentation input. The tested input
for the original archive replay is `aptech/docs` archive/qthelp commit
`7c9e3736fd4c7e557b69e2e6c0c127efc528b69f`. The original local qthelp and its remote
tracking branch differed from this revision. Do not substitute master or a moving
branch. No unrelated source-workspace changes belong in the bundle.

The complete packaging owner is:

```text
janus:/home/jason/svn/21/x64/html5docsync.new
svn+ssh://svnext/data/rep/guiroot/helpgen/trunk
working-copy revision 6942; last changed revision 6925
```

**SVN alone is insufficient.** HTML5 and gauss.qhcp are untracked; welcome.html
and mkhelp.sh are modified. Preserve the snapshot and its manifest as an input
artifact. The packaging Python scripts, properties header/tail, welcome pages,
fonts, HTML5 assets, QHCP and existing baseline QCH/QHC are all explicit inputs.
The old mkhelp.sh is captured for provenance but is never executed.

Read-only acquisition example (run on a machine that can SSH to Janus):

```sh
mkdir -p source-snapshot/packaging source-snapshot/baseline
rsync -a --relative \
  janus:/home/jason/svn/21/x64/html5docsync.new/./HTML5 \
  janus:/home/jason/svn/21/x64/html5docsync.new/./etc \
  janus:/home/jason/svn/21/x64/html5docsync.new/./clean_sphinx.py \
  janus:/home/jason/svn/21/x64/html5docsync.new/./genhelpproperties.py \
  janus:/home/jason/svn/21/x64/html5docsync.new/./help.py \
  janus:/home/jason/svn/21/x64/html5docsync.new/./help.properties.head \
  janus:/home/jason/svn/21/x64/html5docsync.new/./help.properties.tail \
  janus:/home/jason/svn/21/x64/html5docsync.new/./gauss.qhcp \
  janus:/home/jason/svn/21/x64/html5docsync.new/./mkhelp.sh \
  janus:/home/jason/svn/21/x64/html5docsync.new/./requirements.txt \
  source-snapshot/packaging/
rsync -a janus:/home/jason/svn/21/x64/html5docsync.new/gauss.qch \
  janus:/home/jason/svn/21/x64/html5docsync.new/gauss.qhc source-snapshot/baseline/
```

Record the actual owner/revision/local changes in a JSON file, then:

```sh
python3 app-help/prepare.py \
  --docs-repo /path/to/aptech-docs \
  --docs-revision f7b290e34a849af3d1670ad52d0c521e54ec0090 --release 27 \
  --packaging source-snapshot/packaging \
  --baseline source-snapshot/baseline \
  --packaging-provenance packaging-provenance.json \
  --output inputs-27
```

Preparation exports committed docs (ignoring dirty working files), fetches fixed
theme/textbook/tspdlib revisions and downloads SHA256-verified MathJax 2.7.9.
It does not modify any source repository. The resulting `inputs.lock.json` seals
every file. Build verifies it both before and inside the container. Keep that
manifest with the input artifact; changing the manifest constitutes a new input.
The checked-in `evidence/gauss27/inputs.lock.json` records the GAUSS 27 snapshot;
`evidence/inputs.lock.json` records the original archive replay. Compare
its `sha256` mapping with a newly prepared bundle before claiming an exact replay;
preparation intentionally seals the caller's chosen packaging snapshot rather
than assuming today's mutable checkout still has the tested bytes.

`--release 27` rejects a source whose first changelog section is not 27.x.
The sealed release also sets Sphinx's version and the staged welcome heading;
output validation checks all three. This changes no source checkout and preserves
the compatible legacy help namespace. To replay the original GAUSS 26 archive,
use commit `7c9e3736fd4c7e557b69e2e6c0c127efc528b69f` and omit `--release`.

Pinned supporting sources:

| Input | Revision | Why |
|---|---|---|
| sphinx_rtd_theme checkout | d64dadf1ceec4f9ff6c1ca2d3ea4c3d0fdb0e8d2 | Reproduce archive tree; installed 0.5.2 is the effective theme |
| gauss-textbook-examples | 68800eb0782bb9d3dc8354ed19bc4084525a758f | Archive source dependency |
| tspdlib | ed4199d0a6821604940a108aa4664813ae551843 | Untracked by docs parent but required by applications card |
| MathJax | 2.7.9; SHA256 in inputs.py | Complete offline loader/config/fonts; old build omitted the referenced tree |

The archive's untracked g25_theme_override.css and theme_override.css.bak are not
referenced by its configuration and are excluded. The tracked theme_override.css
is included. Preparation does not need access to the `apt` server.

## Application pipeline example

An application build job can generate into its own artifact directory, then stage
the validated pair in its **unpublished build tree**:

```sh
set -eu
: "${HELP_INPUTS:?prepared immutable input bundle}"
: "${BUILD_ARTIFACTS:?isolated artifact root}"
: "${APP_STAGING:?unpublished application staging directory}"
./app-help/build.sh --inputs "$HELP_INPUTS" \
  --output "$BUILD_ARTIFACTS/app-help" --jobs 2 --memory 4g
mkdir -p "$APP_STAGING/help"
install -m 644 "$BUILD_ARTIFACTS/app-help/gauss.qch" "$APP_STAGING/help/gauss.qch"
install -m 644 "$BUILD_ARTIFACTS/app-help/gauss.qhc" "$APP_STAGING/help/gauss.qhc"
```

No CI job, release switch, installed application, website alias or SVN commit is
enabled by this example. Runtime search indexing requires a writable collection,
as the existing application already expects.

## Validation and compatibility

`validate.py` reads and decompresses actual QCH database resources, checks SQLite
integrity, collection registration, namespace, TOC targets, command identifiers,
representative content, HTML/CSS resources and changes against the old baseline.
Existing broken links are reported separately from new regressions.

`qt_probe.py` opens a relocated copy using Qt Help, rebuilds the full-text index,
searches for regression, resolves context help, and renders welcome, command,
math, legacy guide and plot-image pages using Qt WebKit. It denies outbound requests and
captures screenshots. Search indexes never modify the delivered QHC.

For a consumer built with the application's own Qt installation:

```sh
mkdir native-probe disposable-help
cp /path/to/output/gauss.qch /path/to/output/gauss.qhc disposable-help/
cd native-probe
/path/to/application-qt/bin/qmake /path/to/app-help/qt_compat.pro
make -j2
QT_QPA_PLATFORM=offscreen ./qt_compat ../disposable-help /path/to/evidence
```

The preserved namespace is `com.aptech.gauss.25.0`, matching the baseline even
though content says GAUSS 26. Tests explicitly check the application's different
home URL (`qthelp://aptech.com.gauss.26.0/doc/welcome.html`) via Qt's resolution.
Do not rename the namespace as an incidental containerization change.

Qt documents the [QCH/QHC architecture](https://doc.qt.io/qt-6.8/qthelp-framework.html)
and [help-engine resource lookup](https://doc.qt.io/qt-6.8/qhelpenginecore.html).
Compatibility claims here come from the actual Qt 5 probes, not Qt 6 documentation.

See `VALIDATION.md` for measured results, limitations and exact artifact locations.
