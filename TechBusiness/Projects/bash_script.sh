#!/usr/bin/env bash
set -e

echo "[BASH] Running maintenance checks"
echo "- Checking disk space"
df -h | head -n 5
echo "- Checking current user"
whoami
echo "- Status: ready"
