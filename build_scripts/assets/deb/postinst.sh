#!/usr/bin/env bash
# Post install script for the UI .deb to place symlinks in places to allow the CLI to work similarly in both versions

set -e

ln -s /usr/lib/<PUSSY2>/resources/app.asar.unpacked/daemon<PUSSY5> /usr/bin<PUSSY5> || true
ln -s /usr/lib/<PUSSY2>/resources/app.asar.unpacked/daemon /opt<PUSSY5> || true
