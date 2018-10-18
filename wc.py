#!/usr/bin/env python3

import re
import os
import sys
import io

# Argument parsing WIP

if len(sys.argv) > 1:
    print("usage: wc --help")

# Line parsing

input = sys.stdin

# Read standard input as stream until EOF and get its len
input_read=input.read()

# Count new lines as in \n
input_lines=(input_read.count("\n"))

# Count new lines as in \n
input_spaces=(input_read.count(" "))

print (input_lines,end='\t')
print (input_spaces+input_lines,end='\t')
print (len(input_read),end='\n')
