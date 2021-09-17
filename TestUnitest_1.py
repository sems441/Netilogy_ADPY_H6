import unittest
from main import people_name, del_doc, add_shelf
from unittest.mock import patch


class TestUnitest(unittest.TestCase):
    @patch('builtins.input', lambda *args: '11-2')
    def test_people_name(self):
        self.assertEqual(people_name(), "Геннадий Покемонов")

    @patch('builtins.input', lambda *args: '1')
    def test_add_shelf(self):
        self.assertEqual(add_shelf(), False)

    @patch('builtins.input', lambda *args: '10006')
    def test_del_doc(self):
        self.assertEqual(del_doc(), '10006')