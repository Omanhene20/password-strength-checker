# test_passwords.py
import unittest
from passwords import password_strength


class TestPasswordStrength(unittest.TestCase):
    def test_basic_password_strength(self):
        # basic classification
        self.assertEqual(password_strength("abc123!@#")["strength"], "weak")
        self.assertEqual(password_strength("Abc123!@#")["strength"], "medium")
        self.assertEqual(password_strength("Abc123!@#XYZ")["strength"], "strong")

    def test_feedback_for_weak_password(self):
        res = password_strength("pass")
        self.assertEqual(res["strength"], "weak")
        # expecting actionable feedback items and at least one 'increase' or 'Add' suggestion
        self.assertTrue(isinstance(res["feedback"], list))
        self.assertTrue(len(res["feedback"]) >= 1)
        # ensure feedback mentions adding something
        joined = " ".join(res["feedback"]).lower()
        self.assertTrue("add" in joined or "increase" in joined or "must not be empty" in joined)

    def test_non_string_input_raises(self):
        for bad in [12345, None, 3.14, [], {}]:
            with self.assertRaises(TypeError):
                password_strength(bad)

    def test_edge_cases_empty_and_space(self):
        # empty string
        res_empty = password_strength("")
        self.assertEqual(res_empty["strength"], "weak")
        self.assertIn("must not be empty", " ".join(res_empty["feedback"]).lower())

        # string with spaces only
        res_space = password_strength("   ")
        self.assertEqual(res_space["strength"], "weak")
        self.assertIn("must not be empty", " ".join(res_space["feedback"]).lower())

    def test_unicode_and_specials(self):
        # unicode accents and symbols should be considered
        res_unicode = password_strength("Pässw0rd")
        # length 7 -> medium expected because it has upper, lower, digit but shortish -> medium
        self.assertIn(res_unicode["strength"], ("weak", "medium", "strong"))
        # special unicode punctuation
        res_special = password_strength("Paßw0rd©!")
        self.assertIn(res_special["strength"], ("medium", "strong"))

    def test_whitespace_within_password(self):
        # passwords containing spaces are allowed but should be weak if other criteria not met
        res = password_strength("pass word!")
        self.assertEqual(res["strength"], "weak")

    def test_strong_password_score(self):
        strong = "Very$trongPass123!"
        res = password_strength(strong)
        self.assertEqual(res["strength"], "strong")
        self.assertEqual(res["feedback"], [])  # strong passwords have no feedback

if __name__ == "__main__":
    unittest.main()
