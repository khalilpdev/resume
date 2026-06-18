#!/usr/bin/env bash

set -euo pipefail

branch="$(git symbolic-ref --quiet --short HEAD 2>/dev/null || true)"

if [[ -z "$branch" ]]; then
  echo "❌ Commits in detached HEAD are blocked."
  echo "   Checkout a feature branch before committing."
  exit 1
fi

if [[ "$branch" == "main" || "$branch" == "master" ]]; then
  echo "❌ Direct commits to '$branch' are blocked."
  echo "   Create a feature branch before committing."
  exit 1
fi
