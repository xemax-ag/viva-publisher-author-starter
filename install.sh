#!/usr/bin/env bash
# Installs or updates uv, then installs Python and a .venv on Linux.
# No root rights needed.
# The Python version comes from .python-version next to this file, the
# packages from pyproject.toml. Run it again to pick up new packages.
#
# Usage: ./install.sh [folder]
#   Creates folder/.venv. Without a folder: .venv in the current folder.
set -uo pipefail

fail() {
    echo
    echo "Installation failed, see the messages above."
    exit 1
}

# Resolve the target folder before changing directory, so relative paths work.
TARGET="${1:-$PWD}"
case "$TARGET" in
    /*) ;;
    *) TARGET="$PWD/$TARGET" ;;
esac
TARGET="${TARGET%/}"
VENV="$TARGET/.venv"

cd "$(dirname "${BASH_SOURCE[0]}")" || fail

UV_BIN="${XDG_BIN_HOME:-$HOME/.local/bin}"

if ! command -v uv >/dev/null 2>&1; then
    # The installer updates PATH for new shells only; make uv usable here too.
    export PATH="$UV_BIN:$PATH"
fi

if command -v uv >/dev/null 2>&1; then
    echo "=== Checking for uv updates ==="
    # Fails if uv came from a package manager or pip; then keep the installed version.
    uv self update || echo "uv was not updated, continuing with the installed version."
else
    echo "=== Installing uv ==="
    if command -v curl >/dev/null 2>&1; then
        curl -LsSf https://astral.sh/uv/install.sh | sh || fail
    elif command -v wget >/dev/null 2>&1; then
        wget -qO- https://astral.sh/uv/install.sh | sh || fail
    else
        echo "Neither curl nor wget found, please install one of them."
        fail
    fi
fi

uv --version || fail

echo
echo "=== Installing Python ==="
uv python install --default || fail

echo
echo "=== Resolving packages from pyproject.toml ==="
# Errors in pyproject.toml stop here, before the .venv is touched.
uv lock || fail

echo
echo "=== Creating or updating $VENV ==="
# Creates the .venv if missing, then installs, updates or removes packages
# so they match the dependencies in pyproject.toml (pinned in uv.lock).
export UV_PROJECT_ENVIRONMENT="$VENV"
if ! uv sync; then
    echo
    echo "=== Updating failed, removing and recreating $VENV ==="
    if ! rm -rf "$VENV"; then
        echo "Could not remove $VENV."
        echo "Close all programs that use it, or remove it yourself, then run this again."
        fail
    fi
    uv sync || fail
fi

echo
"$VENV/bin/python" --version || fail
echo "Done. Open a new terminal to use uv and python."
