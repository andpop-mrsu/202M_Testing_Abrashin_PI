import unittest

from triangle_func import IncorrectTriangleSides, get_triangle_type

class TestGetTriangleType(unittest.TestCase):
    def test_equilateral_triangle(self):
        self.assertEqual(get_triangle_type(10, 10, 10), 'equilateral')

    def test_isosceles_triangle(self):
        self.assertEqual(get_triangle_type(5, 5, 4), 'isosceles')

    def test_nonequilateral_triangle(self):
        self.assertEqual(get_triangle_type(7, 8, 9), 'nonequilateral')

    def test_negative_side_length(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(-5, 7, 9)

    def test_impossible_triangle(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(5, 10, 100)

    def test_zero_side_length(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(1, 0, 6)

if __name__ == '__main__':
    unittest.main()