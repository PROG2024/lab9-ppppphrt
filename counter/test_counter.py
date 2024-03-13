"""Write a unit test to verify that Counter is a singleton.

   Also verify that all instances share the same count
   and that the count is not reset to 0 when you invoke 
   count = Counter() 
   after the first time.

   You can use pytest or unittest.
"""
import unittest
from counter import Counter


class TestCounter(unittest.TestCase):
    def test_singleton(self):
        c1 = Counter()
        c2 = Counter()
        self.assertIs(c1, c2)
        self.assertEqual(c1.count, 0)
        self.assertEqual(c2.count, 0)
        c1.increment()
        self.assertEqual(c2.count, 1)
        c2.increment()
        self.assertEqual(c1.count, 2)