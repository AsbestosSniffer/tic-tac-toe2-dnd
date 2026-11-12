from unittest import TestCase
from cli import Cli, ErrorMsgs

class TestCli(TestCase):

    def test_reject_malformed_input(self):
        cli = Cli()
        cli.prompt('badtest')
        self.assertEqual(cli.current_printed(), ErrorMsgs.INVALID_INPUT)