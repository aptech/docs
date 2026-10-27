#!/usr/bin/env bash
# Artifact generation only. Image/input preparation are deliberately separate.
set -euo pipefail
usage() { echo "Usage: $0 --inputs DIR --output EMPTY_DIR [--image IMAGE] [--runtime podman|docker] [--jobs 2] [--memory 4g]" >&2; exit 2; }
image=localhost/gauss-app-help:validation
jobs=2
memory=4g
runtime=${CONTAINER_RUNTIME:-}
inputs=
output=
while (($#)); do
    (($# >= 2)) || usage
    case "$1" in
        --inputs) inputs=$2;;
        --output) output=$2;;
        --image) image=$2;;
        --runtime) runtime=$2;;
        --jobs) jobs=$2;;
        --memory) memory=$2;;
        *) usage;;
    esac
    shift 2
done
[[ -n "$inputs" && -n "$output" ]] || usage
[[ "$jobs" =~ ^[0-9]+$ ]] && ((jobs >= 1 && jobs <= 16)) || usage
if [[ -z "$runtime" ]]; then
    if command -v podman >/dev/null; then runtime=podman; else runtime=docker; fi
fi
[[ "$runtime" == podman || "$runtime" == docker ]] || usage
inputs=$(cd "$inputs" && pwd -P)
mkdir -p "$output"
output=$(cd "$output" && pwd -P)
[[ -z "$(ls -A "$output")" ]] || { echo 'Output must be empty' >&2; exit 2; }
case "$output/" in "$inputs/"*) echo 'Output must be outside inputs' >&2; exit 2;; esac
recipe=$(cd "$(dirname "$0")" && pwd -P)
python3 "$recipe/inputs.py" verify "$inputs"
image_id=$("$runtime" image inspect "$image" --format '{{.Id}}')
scratch=$(mktemp -d "${TMPDIR:-/tmp}/gauss-app-help.XXXXXXXX")
log=$(mktemp "${TMPDIR:-/tmp}/gauss-app-help-log.XXXXXXXX")
trap 'rm -rf "$scratch"; rm -f "$log"' EXIT
user_args=(--user "$(id -u):$(id -g)")
if [[ "$runtime" == podman ]]; then user_args+=(--userns keep-id); fi
set +e
"$runtime" run --rm --pull=never --network=none --read-only \
    --cap-drop=ALL --security-opt=no-new-privileges --security-opt=label=disable \
    --memory "$memory" --memory-swap "$memory" --pids-limit 256 \
    "${user_args[@]}" --tmpfs /tmp:rw,nosuid,nodev,size=256m \
    -e HOME=/tmp -e XDG_RUNTIME_DIR=/tmp/runtime \
    -v "$inputs:/inputs:ro" -v "$output:/out:rw" -v "$scratch:/scratch:rw" \
    "$image_id" --jobs "$jobs" 2>&1 | tee "$log"
rc=${PIPESTATUS[0]}
set -e
cp "$log" "$output/build.log"
printf '%s\n' "$image_id" > "$output/image-id.txt"
if ((rc)); then
    echo "Build failed ($rc); diagnostics retained in $output" >&2
    exit "$rc"
fi
echo "Validated help: $output/gauss.qch and $output/gauss.qhc"
