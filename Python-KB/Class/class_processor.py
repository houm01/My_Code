#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# github: https://github.com/houm01


def processor(reader, converter, writer):
    while 1:
        data = reader.read()
        if not data:
            break
        data = converter(data)
        writer.write(data)


class Reader:
    def read(self): ...
    def other(self): ...
class FileReader(Reader):
    def read(self): ...
class SocketReader(Reader):
    def read(self): ...
...

processor(FileReader(...), Converter, FileWriter(...))
processor(SocketReader(...), converter, TapeWriter(...))
processor(FtpReader(...), Converter, XmlWriter(...))

