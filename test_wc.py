#!/usr/bin/env python3
import unittest
import io
from wc import input_parse

class TestStringMethods(unittest.TestCase):

    def test_three_words(self):
        test_in = io.StringIO("uno1 dos2 tres3\n")
        self.assertEqual(input_parse(test_in), (1, 3, 16))

    def test_three_words_two_lines(self):
        test_in = io.StringIO("uno1 dos2 tres3\n.. cuatro  cinco\n")
        self.assertEqual(input_parse(test_in), (2, 6, 33))

    def test_three_linesi_and_words(self):
        test_in = io.StringIO("uno1 dos2 tres3\n.. cuatro  cinco\nsix  7 9 ten. \n")
        self.assertEqual(input_parse(test_in), (3, 10, 48))




if __name__ == '__main__':
    unittest.main()
