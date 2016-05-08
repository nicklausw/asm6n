#!/usr/bin/env python3

# takes in a file, c++ to c
# comments.

import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("in_file")
parser.add_argument("out_file")
args = parser.parse_args()

f_in = open(args.in_file, 'r')
f_out = open(args.out_file, 'w')

line = f_in.readline()

while line:
  if line.find('//') != -1:
    line = line.replace('//', '/*')
    line = line.replace('\n', ' */\n')
  f_out.write(line)
  line = f_in.readline()

f_in.close()
f_out.close()
