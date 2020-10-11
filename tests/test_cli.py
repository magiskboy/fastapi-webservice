from unittest import TestCase
from click.testing import CliRunner
from app.__main__ import cli


class CommandLineTestCase(TestCase):
    def setUp(self):
        self.runner = CliRunner()


class RoutesCommandTestCase(CommandLineTestCase):
    def test_get_success(self):
        result = self.runner.invoke(cli, ['routes'])
        assert result.exit_code == 0, result.exception
