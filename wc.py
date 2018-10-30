#!/usr/bin/env python3

import sys
import io
import re
import argparse
import click
import requests

class wc:
    def __init__(self):
        self.count_of_lines = 0
        self.count_of_words = 0
        self.count_of_bytes = 0
     
    def input_parse(self, data_input):
        # Read standard input as a stream until EOF and get its length 
        self.input_read=data_input.read()

    def input_parse_content(self, data_input):
        # Read standard input as a stream until EOF and get its length 
        self.input_read=(data_input.text)


    def count_newlines(self):
        # Count new line character 
        self.count_of_lines=(self.input_read.count("\n"))


    def count_words(self):
        # Count words from regex
        self.count_of_words=len(re.findall('\S+', self.input_read))


    def count_bytes(self):
        self.count_of_bytes=len(self.input_read)

        # Print everything here from a parameter string
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

# Argument parsing
@click.command()
@click.option('-c', '--bytes','cbytes' ,help='print the word counts',is_flag=True)
@click.option('-l', '--lines',  help='print the newline counts',is_flag=True)
@click.option('-w', '--words',  help='print the byte counts',is_flag=True)
@click.option('-e', 'url',  help='print the word counts from a url')
 
def read_parameters(cbytes,lines,words,url):
    options = ""

    if lines:
        options = options + "l"
    if words:
        options = options + "w"
    if url:
        count_url(url,"w")
    if cbytes:
        options = options + "c"
    
    data_input = sys.stdin

    a_wc = wc()
    a_wc.input_parse(data_input)
    a_wc.print_wc_like_count(options)

def count_url(link, options):
    r = requests.get(link)

    a_wc = wc()
    a_wc.input_parse_content(r)
    a_wc.print_wc_like_count(options)
    sys.exit(0)

#Use module as an script
if __name__ == '__main__':

    data_input = sys.stdin

    a_wc = wc()

    if len(sys.argv) == 1:
        option = "lwc"
        a_wc.input_parse(data_input)
        a_wc.print_wc_like_count(option)
        sys.exit(0)

    read_parameters()
