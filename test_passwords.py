import unittest
from passwords import password_strength

class PasswordStrengthTest(unittest.TestCase):
def test_empty_is_weak(self):
self.assertEqual(password_strength(""), "weak")

def test_letters_only_short(self):
    self.assertEqual(password_strength("abcdefg"), "weak")
    
def test_letters_and_digits_medium(self):
    self.assertEqual(password_strength("abc12345"), "medium")
    
def test_letters_digits_symbol_strong(self):
    self.assertEqual(password_strength("abc12345!!xx"), "strong")

def test_non_string_input(self):
    with self.assertRaises(TypeError):
        password_strength(123)
if name == "main":

unittest.main()
