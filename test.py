import unittest
from main import game_init

class Test(unittest.TestCase):
    def test_place_your_mark_on_an_empty_cell(self):
        game = game_init()
        player = game.player_init()
        self.assertTrue(player.place_mark(0, 0))

    def test_player_tries_to_mark_out_of_turn(self):
        game = game_init()
        player = game.player_init()
        player.place_mark(0, 1)
        self.assertTrue(player.place_mark(0, 0) == False)

    def test_player2_cannot_go_first(self):
        game = game_init()
        player1 = game.player_init()
        player2 = game.player_init() 
        self.assertFalse(player2.place_mark(0, 0))

    def test_player_placing_a_mark_ends_turn(self):
        game = game_init()
        player1 = game.player_init()
        player2 = game.player_init() 
        player1.place_mark(0, 0)

        self.assertTrue(player2.place_mark(0, 1))

    def test_place_mark_on_occupied_cell(self):
        game = game_init()
        player1 = game.player_init()
        player2 = game.player_init()
        player1.place_mark(0,0)
        self.assertFalse(player2.place_mark(0,0))

    def test_player2_cannot_move_after_player1_wins_case1(self):
        game = game_init()
        player1 = game.player_init()
        player2 = game.player_init()
        player1.place_mark(0,0)
        player2.place_mark(1,0)
        player1.place_mark(0,1)
        player2.place_mark(1,1)
        player1.place_mark(0,2)
        self.assertFalse(player2.place_mark(1,2))