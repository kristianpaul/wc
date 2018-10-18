#!/usr/bin/env python3

import sys
import io
import re

# Argument parsing WIP

def input_parse():
    if len(sys.argv) > 1:
        print("usage: wc --help")
    
    input=sys.stdin

    # Read standard input as a stream until EOF and get its length 
    input_read=input.read()
    # Count new line character 
    count_of_lines=(input_read.count("\n"))
    # Count words from regex
    count_of_words=len(re.findall('\w+', input_read))
    count_of_bytes=len(input_read)

    return count_of_lines,count_of_words,count_of_bytes

def print_wc_like_count():
    try:
        for  i in input_parse():
            print(i,end='\t')
    finally:
        print('\n')

print_wc_like_count()
