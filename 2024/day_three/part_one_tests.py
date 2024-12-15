# python3 -m unittest part_one_tests.py
import unittest
from part_one import regex_finder

class RegexFinderTest(unittest.TestCase):
    def test_no_match(self):
        # no results in regex without match
        result = regex_finder('hello')
        self.assertEqual(result, 0)

    def test_one_match(self):
        # one result in regex with only one match
        result = regex_finder('mul[3,7]!@^do_not_mul(5,5)')
        self.assertEqual(result, 1)

    def test_two_matches(self): 
        input = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
        result = regex_finder(input)
        self.assertEqual(result, 4)
