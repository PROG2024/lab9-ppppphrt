"""Unit tests of the Circle class using unittest or pytest (your choice).

Write unit tests as described in README.md.

1. Unit test for add_area using typical values.
2. Unit test for add_area for an "edge case" where one circle has radius 0.
3. Unit test that circle constructor raises exception of radius is negative.

"""
import unittest
import sys

from circle import Circle


class TestCircle(unittest.TestCase):
    def test_add_area_typical(self):
        c1 = Circle(1)
        c2 = Circle(2)
        self.assertEqual(c1.add_area(c2), 12.566370614359172)

    def test_add_area_edge_case(self):
        c1 = Circle(0)
        c2 = Circle(2)
        self.assertEqual(c1.add_area(c2), 12.566370614359172)

    def test_circle_constructor(self):
        with self.assertRaises(ValueError):
            c1 = Circle(-1)
            c2 = Circle(-111)
            c3 = Circle(-1 * sys.float_info.max)
