from unittest import TestCase
from cli import Cli, CliMsgs

class TestCli(TestCase):

    def test_reject_malformed_input(self):
        cli = Cli()
        cli.prompt('badtest')
        self.assertEqual(cli.current_printed(), CliMsgs.INVALID_INPUT)

    def test_accept_correct_input(self):
        cli = Cli()
        cli.prompt('x12')
        self.assertIsNone(cli.current_printed())