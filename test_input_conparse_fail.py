#!/usr/bin/env python3

#test_input_conparse.py

import unittest
from input_conparse import InputReader

class TestInputReader(unittest.TestCase):
    """ This is a test class for testing the input_conparse module. """
    def test_input_reader_class(self):
        instance = InputReader('test_pars_fail.inp')
        self.assertFalse(instance.parse_success)

if __name__ == '__main__':
    unittest.main()
