import random
from collections import Counter as cnt
from unittest import TestCase, main

from whiteboard import solution

class MatchTestCase(TestCase):
    def test_example_one(self):
        self.assertEqual(solution("hello","aaahello"), 'a')
    def test_example_two(self):
        self.assertEqual(solution("abcde","2db2a2ec"), '2')
    def test_exapmle_three(self):
        self.assertEqual(solution("aabbcc","aacccbbcc"), "c")