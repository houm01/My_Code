#!/bin/bash

echo '$*------------':
for i in $*;do echo "<$i>"; done

echo '"$*------------"':
for i in "$*";do echo "<$i>";done


echo '$@------------':
for i in $@;do echo "<$i>"; done

echo '"$@------------"'
for i in "$@"; do echo "<$i>";done
