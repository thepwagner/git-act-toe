#!/bin/sh

set -o pipefail
set -e

git config --global user.name "Git Act Toe"
git config --global user.email "git-act-toe@mycloudand.me"

python3 -m "gat.action" | tee game.txt
git commit game.txt -m "turn"
git remote -v
git push -u origin $(echo $GITHUB_REF | sed s@refs/heads/@@g)
