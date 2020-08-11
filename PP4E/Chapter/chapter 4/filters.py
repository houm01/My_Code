#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# github: https://github.com/houm01


import sys

# 第一种写法
# def filter_files(name, function):
#     input = open(name, 'r')
#     output = open(name + '.out', 'w')
#     for line in input:
#         output.write(function(line))
#     input.close()
#     output.close()


# 第二种写法
def filter_files(name, function):
    with open(name, 'r') as input, open(name + '.out', 'w') as output:
        for line in input:
            output.write(function(line))


# 第一种写法
# def filter_stream(function):
#     while True:
#         line = sys.stdin.readline()
#         if not line:
#             break
#         print(function(line), end='')


# 第二种写法
def filter_stream(function):
    for line in sys.stdin:
        print(function(line), end='')


if __name__ == '__main__':
    filter_stream(lambda line: line)

