import unittest
from main import player_init

class Test(unittest.TestCase):
    def test_example(self):
        self.assertEqual(True, True)

    def test_place_your_mark_on_an_empty_cell(self):
        player = player_init()
        self.assertTrue(player.place_mark(0, 0))

    def test_player_tries_to_mark_out_of_turn(self):
        player2 = player_init()
        player2.place_mark(0, 1)
        self.assertTrue(player2.place_mark(0, 0) == False)
        