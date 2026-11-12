from unittest import TestCase
from cli import Cli, CliMsgs
from main import game_init

class TestCli(TestCase):

    def test_malformed_input_prints_error(self):
        game = game_init()
        cli = Cli(game)
        cli.prompt('badtest')
        self.assertEqual(cli.current_printed(), CliMsgs.INVALID_INPUT)

    def test_correct_input_no_error(self):
        game = game_init()
        cli = Cli(game)
        cli.prompt('x12')
        self.assertIsNone(cli.current_printed())

    def test_player1_win_prints_game_end_and_correct_winner(self):
        game = game_init()
        cli = Cli(game)
        cli.prompt('x00')
        cli.prompt('o10')
        cli.prompt('x01')
        cli.prompt('o11')
        cli.prompt('x02')
        self.assertEqual(cli.current_printed(), CliMsgs.PLAYER1_WIN)