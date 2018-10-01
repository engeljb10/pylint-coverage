"""
Unnittest of Triangle.py

author: Jack Engel
"""

import unittest

from triangle import classify_triangle

class TestTriangles(unittest.TestCase):
    """
    contains tests for triangle
    """

    def test_right_triangle_a(self):
        """
        tests right triangle A
        """
        self.assertEqual(classify_triangle(3, 4, 5), 'Right', '3,4,5 is a Right triangle')

    def test_right_triangle_b(self):
        """
        tests right triangle B
        """
        self.assertEqual(classify_triangle(5, 3, 4), 'Right', '5,3,4 is a Right triangle')

    def test_equilateral_triangles(self):
        """
        tests equilateral triangle
        """
        self.assertEqual(classify_triangle(1, 1, 1), 'Equilateral', '1,1,1 should be equilateral')

    def test_isosceles_triangles(self):
        """
        tests isoscle triangle
        """
        self.assertEqual(classify_triangle(3, 3, 4), 'Isosceles', '3,3,4 should be isosceles')

    def test_scalene_triangles(self):
        """
        tests scalene triangle
        """
        self.assertEqual(classify_triangle(2, 3, 4), 'Scalene', '2,3,4 should be scalene')

    def test_not_a_triangle(self):
        """
        tests not a triangle
        """
        self.assertEqual(classify_triangle(2, 3, 9), 'NotATriangle', '2,3,9 is not a triangle')

    def test_invalid_input_int(self):
        """
        tests invalid input for triangle
        """
        self.assertEqual(classify_triangle(2.5, 3, 9), 'InvalidInput', '2.5 is not an integer')

    def test_invalid_input_zero(self):
        """
        tests inavlid value of 0 for triangle
        """
        self.assertEqual(classify_triangle(0, 3, 5), 'InvalidInput', '0 is invalid')

    def test_invalid_input200(self):
        """
        tests exceeding max input for triangle
        """
        self.assertEqual(classify_triangle(201, 3, 2), 'InvalidInput', '201 exceeds maximum input')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
