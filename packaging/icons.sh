#!/usr/bin/env bash
# Rebuild app icon assets from assets/app-icon/tabdocs-source.png.
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
python3 "$ROOT/packaging/generate-icons.py"
