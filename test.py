import unittest
from main import game_init, GameStatus

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

        # X X X
        # O O *
        # _ _ _

        player1.place_mark(0,0)
        player2.place_mark(1,0)
        player1.place_mark(0,1)
        player2.place_mark(1,1)
        player1.place_mark(0,2)
        self.assertFalse(player2.place_mark(1,2))

    def test_player1_cannot_move_after_player2_wins(self):
        game = game_init()
        player1 = game.player_init()
        player2 = game.player_init()
           
        # X X *
        # O O O
        # X _ _

        player1.place_mark(0,0)
        player2.place_mark(1,0)
        player1.place_mark(0,1)
        player2.place_mark(1,1)
        player1.place_mark(2,0)
        player2.place_mark(1,2)
        self.assertFalse(player1.place_mark(0,2))

    # program can detect someone won but not who

    def test_detect_player1_win(self):
        game = game_init()
        player1 = game.player_init()
        player2 = game.player_init()

        # X O _
        # X O _
        # X _ _

        player1.place_mark(0,0)
        player2.place_mark(0,1)
        player1.place_mark(1,0)
        player2.place_mark(1,1)
        player1.place_mark(2,0)
        status = game.get_result()
        self.assertEqual(status, GameStatus.PLAYER1_WINS)

    
    def test_detect_player2_win(self):
        game = game_init()
        player1 = game.player_init()
        player2 = game.player_init()

        # X O X
        # X O _
        # _ O _

        player1.place_mark(0,0)
        player2.place_mark(0,1)
        player1.place_mark(1,0)
        player2.place_mark(1,1)
        player1.place_mark(0,2)
        player2.place_mark(2,1)
        status = game.get_result()
        self.assertEqual(status, GameStatus.PLAYER2_WINS)

    def test_detect_draw(self):
        game = game_init()
        player1 = game.player_init()
        player2 = game.player_init()

        # X O X
        # X O O
        # O X X

        player1.place_mark(0,0)
        player2.place_mark(0,1)
        player1.place_mark(1,0)
        player2.place_mark(1,1)
        player1.place_mark(0,2)
        player2.place_mark(2,0)
        player1.place_mark(2,1)
        player2.place_mark(1,2)
        player1.place_mark(2,2)
        status = game.get_result()
        self.assertEqual(status, GameStatus.DRAW)