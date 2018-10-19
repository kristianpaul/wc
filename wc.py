#!/usr/bin/env python3

import sys
import io
import re
import argparse

# Argument parsing WIP

def argument_parse():
    option=""
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--lines", help="print the newline counts", action="store_true")
    parser.add_argument("-w", "--words", help="print the newline counts", action="store_true")
    parser.add_argument("-c", "--bytes", help="print the byte counts", action="store_true")
    args = parser.parse_args()
    if args.lines:
        option=option+"l"
    if args.words:
        option=option+"w"
    if args.bytes:
        option=option+"c"
    return option

def input_parse(data_input):
    
    # Read standard input as a stream until EOF and get its length 
    input_read=data_input.read()
    # Count new line character 
    count_of_lines=(input_read.count("\n"))
    # Count words from regex
    count_of_words=len(re.findall('\S+', input_read))
    count_of_bytes=len(input_read)

    return count_of_lines,count_of_words,count_of_bytes

def print_wc_like_count(data_input,parameter):
    if re.match('.*l.*', parameter):
                    print(data_input[0],end='\t')

    if re.match('.*w.*', parameter):
                    print(data_input[1],end='\t')

    if re.match('.*c.*', parameter):
                    print(data_input[2],end='\t')
    print('\n')

#Use module as an script
if __name__ == '__main__':
    option=argument_parse()
    data_input=sys.stdin
    print_wc_like_count(input_parse(data_input),option)
