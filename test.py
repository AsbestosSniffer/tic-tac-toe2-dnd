import unittest
from main import game_init

class Test(unittest.TestCase):
    def test_place_your_mark_on_an_empty_cell(self):
        game = game_init()
        player = game.player_init(1)
        self.assertTrue(player.place_mark(0, 0))

    def test_player_tries_to_mark_out_of_turn(self):
        game = game_init()
        player = game.player_init(1)
        player.place_mark(0, 1)
        self.assertTrue(player.place_mark(0, 0) == False)

    def test_player_placing_a_mark_ends_turn(self):
        game = game_init()
        player1 = game.player_init(1)
        player2 = game.player_init(2) 
        self.assertFalse(player2.place_mark(0, 0))

    # def test_player_placing_a_mark_ends_turn(self):
    #     player1 = player_init()
    #     player2 = player_init() 
    #     player1.place_mark(0, 0)
    #     self.assertTrue(player2.place_mark(0, 0))
        