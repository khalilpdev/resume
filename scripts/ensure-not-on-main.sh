#!/usr/bin/env bash

set -euo pipefail

branch="$(git symbolic-ref --quiet --short HEAD 2>/dev/null || true)"

if [[ "$branch" == "main" || "$branch" == "master" ]]; then
  echo "❌ Direct commits to '$branch' are blocked."
  echo "   Create a feature branch before committing."
  exit 1
fi
