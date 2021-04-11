import os
import unittest
from unittest import mock
from _python_automation_tests.dev import C, get_random_digital_string, get_capitalized_env_name


class TestUnittestFramework(unittest.TestCase):
    @mock.patch("dev.random.randint", return_value=15)
    def test_mock_builtin_method(self, mock_randint):
        self.assertEqual(get_random_digital_string(10, 20), "15")
        mock_randint.assert_called_once_with(10, 20)

    @mock.patch("dev.random.randint", side_effect=ValueError)
    def test_mock_builtin_method_exception(self, mock_randint):
        with self.assertRaises(ValueError):
            get_random_digital_string(20, 10)
            mock_randint.assert_called_once_with(20, 10)

    @mock.patch.object(C, "get_random_number", return_value=15)
    def test_mock_instance_method(self, mock_random_number):
        c = C(start=10, end=20)
        self.assertEqual(c.get_random_digital_string(), "15")
        mock_random_number.assert_called_once()

    @mock.patch.dict(os.environ, {'name': "smita"})
    def test_mock_environment_variables(self):
        self.assertEqual(get_capitalized_env_name(), "SMITA")

    def test_magic_mock(self):
        m = mock.MagicMock()
        m.__len__.return_value = 5
        self.assertEqual(len(m), 5)
