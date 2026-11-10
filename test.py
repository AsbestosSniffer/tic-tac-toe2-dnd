import unittest
from main import place_mark

class Test(unittest.TestCase):
    def test_example(self):
        self.assertEqual(True, True)

    def test_place_your_mark_on_an_empty_cell(self):
        place_mark(0, 0)