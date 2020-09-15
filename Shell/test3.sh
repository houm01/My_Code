#!/usr/bin/env bash

source ./color_print.sh

function throw() { echo -e "[-] FATAL: $1\nexit with code 1"; exit 1; }

#title "download..."
#success "download file to /tmp"
#error "down file to /tmp"
 
echo '[.] copying `FILENAME` ...'
cp /etc/fstab "aaa/" || throw 'copy `FILENAME` failed!'
echo '[~] copied `FILENAME`'
echo "[+] success: installed to aaa/"
