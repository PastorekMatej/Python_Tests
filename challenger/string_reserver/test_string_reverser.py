import unittest
from string_reverser import reverse_string

class TestStringReverser(unittest.TestCase):
    def test_basic_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")
        
    def test_empty_string(self):
        self.assertEqual(reverse_string(""), "")
        
    def test_single_character(self):
        self.assertEqual(reverse_string("a"), "a")
        
    def test_with_spaces(self):
        self.assertEqual(reverse_string("hello world"), "dlrow olleh")
        
    def test_with_special_characters(self):
        self.assertEqual(reverse_string("hello!@#"), "#@!olleh")

if __name__ == '__main__':
    unittest.main()
