#!/usr/bin/env python3
import io
from wc import *

def test_word_count():
    test_in = io.StringIO("uno1 dos2 tres3\n")
    a_wc = wc()
    option = "w"
    a_wc.input_parse(test_in)
    assert a_wc.print_wc_like_count(option) == "3   \n\n"

