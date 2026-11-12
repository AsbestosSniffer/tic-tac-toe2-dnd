from unittest import TestCase
from cli import Cli, CliMsgs
from main import Game

class TestCli(TestCase):

    def test_malformed_input_prints_error(self):
        game = Game()
        cli = Cli(game)
        cli.prompt('badtest')
        self.assertEqual(cli.get_to_print(), CliMsgs.INVALID_INPUT)

    def test_correct_input_no_error(self):
        game = Game()
        cli = Cli(game)
        cli.prompt('x12')
        self.assertIsNone(cli.get_to_print())

    def test_player1_win_prints_correct_winner(self):
        game = Game()
        cli = Cli(game)
        cli.prompt('x00')
        cli.prompt('o10')
        cli.prompt('x01')
        cli.prompt('o11')
        cli.prompt('x02')
        self.assertEqual(cli.get_to_print(), CliMsgs.PLAYER1_WIN)

    def test_player2_win_prints_correct_winner(self):
        game = Game()
        cli = Cli(game)
        cli.prompt('x00')
        cli.prompt('o10')
        cli.prompt('x01')
        cli.prompt('o11')
        cli.prompt('x20')
        cli.prompt('o12')
        self.assertEqual(cli.get_to_print(), CliMsgs.PLAYER2_WIN)

    def test_when_game_draws_prints_draw(self):
        game = Game()
        cli = Cli(game)
        cli.prompt('x00')
        cli.prompt('o10')
        cli.prompt('x01')
        cli.prompt('o11')
        cli.prompt('x12')
        cli.prompt('o02')
        cli.prompt('x20')
        cli.prompt('o21')
        cli.prompt('x22')
        self.assertEqual(cli.get_to_print(), CliMsgs.DRAW)

    def test_same_player_tries_to_go_twice(self):
        game = Game()
        cli = Cli(game)
        cli.prompt('x00')
        cli.prompt('x00')
        self.assertEqual(cli.get_to_print(), CliMsgs.WRONG_PLAYER_TURN)