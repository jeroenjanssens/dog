#!/usr/bin/env bash

echo $PATH |
sed -e 's/:/\n/g' |
parallel "find {} -maxdepth 1 -perm +111 -type f 2>/dev/null" |
parallel "basename {}"
sort | uniq
parallel "echo -n {},; man -w 1 {} 2>/dev/null 1>&2 && echo 1 || echo 0"
