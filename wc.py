#!/usr/bin/env python3

import sys
import io
import re

# Argument parsing WIP

def argument_parse():
    if len(sys.argv) > 1:
        print("usage: wc --help")

def input_parse(data_input):
    
    # Read standard input as a stream until EOF and get its length 
    input_read=data_input.read()
    # Count new line character 
    count_of_lines=(input_read.count("\n"))
    # Count words from regex
    count_of_words=len(re.findall('\S+', input_read))
    count_of_bytes=len(input_read)

    return count_of_lines,count_of_words,count_of_bytes

def print_wc_like_count(data_input):
    try:
        for  i in data_input:
            print(i,end='\t')
    finally:
        print('\n')

#Use module as an script
if __name__ == '__main__':
    data_input=sys.stdin
    print_wc_like_count(input_parse(data_input))
