#! /usr/bin/env bash

if [ -d "tests" ]; then
  echo -e "\e[38;5;12mRunning tests..."
  lua tests/main.lua
fi

path=$1

if [ -z "$1" ]; then
  path="$HOME/.local/bin"
fi

mkdir -p "$path"

echo -e "\e[38;5;12mCreating a symlink to cli on \e[38;5;13m$path\e[0m"

ln ./tools/cli.lua "$path/purepkg"

echo -e "\e[38;5;10mSymlink create at \e[38;5;13m$path\e[0m"
