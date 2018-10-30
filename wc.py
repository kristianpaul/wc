#!/usr/bin/env python3

import sys
import io
import re
import argparse

# Argument parsing WIP
def argument_parse():
    if len(sys.argv) == 1:
        return("lwc")
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
 
class wc:
    def __init__(self):
        self.count_of_lines = 0
        self.count_of_words = 0
        self.count_of_bytes = 0
   
    def input_parse(self, data_input):
        # Read standard input as a stream until EOF and get its length 
        self.input_read=data_input.read()

    def count_newlines(self):
        # Count new line character 
        self.count_of_lines=(self.input_read.count("\n"))

    def count_words(self):
        # Count words from regex
        self.count_of_words=len(re.findall('\S+', self.input_read))

    def count_bytes(self):
        self.count_of_bytes=len(self.input_read)
    
    def print_wc_like_count(self, parameter):
        if re.match('.*l.*', parameter):
                        self.count_newlines()
                        print(str(self.count_of_lines),end='\t')
    
        if re.match('.*w.*', parameter):
                        self.count_words()
                        print(str(self.count_of_words),end='\t')
    
        if re.match('.*c.*', parameter):
                        self.count_bytes()
                        print(str(self.count_of_bytes),end='\t')
        print('\n')
    
    #Use module as an script
if __name__ == '__main__':
    a_wc = wc()
    # parse arguments (to be replaced with click)
    option = argument_parse()
    # 
    data_input = sys.stdin
    #
    parsed_data = a_wc.input_parse(data_input)
    #
    a_wc.print_wc_like_count(option)
