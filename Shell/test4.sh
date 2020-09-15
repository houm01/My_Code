#!/usr/bin/env bash

shopt -s globstar

grep 'PATH' /etc/**/httpd.conf

# shopt -s dotglob

# ls ~/*bash_profile