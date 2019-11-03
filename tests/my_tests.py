import unittest
import math
from homework import *


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.width = 5
        self.height = 7
        self.rectangle = Rectangle(self.width, self.height)

    def test_get_rectangle_per(self):
        self.assertEqual(self.rectangle.get_rectangle_perimeter(), 24)

    def test_get_rectangle_square(self):
        self.assertEqual(self.rectangle.get_rectangle_square(), 35)

    def test_get_sum_of_corners(self):
        self.assertEqual(self.rectangle.get_sum_of_corners(3), 270)

    def test_get_sum_of_corners_invalid_arg(self):
        with self.assertRaises(ValueError):
            self.rectangle.get_sum_of_corners(6)

    def test_rectangle_diagonal(self):
        self.assertEqual(self.rectangle.get_rectangle_diagonal(), math.sqrt(74))

    def test_get_radius_of_circumscribed_circle(self):
        self.assertEqual(self.rectangle.get_rectangle_diagonal() / 2, math.sqrt(74) / 2)

    def test_get_radius_of_inscribed_circle(self):
        self.assertEqual(Rectangle(6, 6).get_radius_of_inscribed_circle(), 3)

    def test_get_radus_of_inscrived_circle_such(self):
        with self.assertRaises(ValueError):
            self.rectangle.get_radius_of_inscribed_circle()


if __name__ == '__main__':
    unittest.main()
