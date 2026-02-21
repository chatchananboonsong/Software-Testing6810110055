import unittest
from cat_mouse import cat_and_mouse

class TestCatAndMouse(unittest.TestCase):
    
    def test_cat_b_wins_example_1(self):
        x, y, z = 1, 2, 3
        result = cat_and_mouse(x, y, z)
        self.assertEqual(result, "Cat B")

    def test_mouse_c_escapes_example_2(self):
        x, y, z = 1, 3, 2
        result = cat_and_mouse(x, y, z)
        self.assertEqual(result, "Mouse C")

    def test_cat_b_wins_example_3(self):
        x, y, z = 1, 5, 4
        result = cat_and_mouse(x, y, z)
        self.assertEqual(result, "Cat B")

    def test_cat_a_wins(self):
        x, y, z = 10, 20, 12
        result = cat_and_mouse(x, y, z)
        self.assertEqual(result, "Cat A")

    def test_boundary_values_100(self):
        x, y, z = 1, 100, 70
        result = cat_and_mouse(x, y, z)
        self.assertEqual(result, "Cat B")

    