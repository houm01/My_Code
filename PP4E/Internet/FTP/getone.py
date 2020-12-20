#!/usr/bin/env python3

import os, sys
from getpass import getpass
from ftplib import FTP
from sys import argv


nonpassive = False
filename = 'monkeys.jpg'
dirname = '.'
sitename = 'ftp.houm01.com'
userinfo = ('lutz', getpass('Pswd?'))
if len(sys.argv) > 1:
    filename = sys.argv[1]

print('Connecting...')
connection = FTP(sitename)
connection.login(*userinfo)
connection.cwd(dirname)
if nonpassive:
    connection.set_pasv(False)

print('Downloading...')
localfile = open(filename, 'wb')
connection.retrbinary('RETR ' + filename, localfile.write, 1024)
connection.quit()
localfile.close()


if input('Open file?') in ['Y', 'y']:
    from PP4E.System.Media.playfile import playfile
    playfile(filename)


                            