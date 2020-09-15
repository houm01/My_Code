#!/usr/bin/env bash

function badfunc1() {
  echo $(($1 * $2))
}

if [ $# -eq 2 ]; then
  value=$(badfunc1 $1 $2)
  echo "The result is $value"
else
  echo "Usage: badtest1 a b"
fi
