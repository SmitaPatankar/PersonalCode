import unittest
from count_letter import count_letter

class TestCountLetter(unittest.TestCase):
    def test_count_letter(self):
        self.assertEqual(count_letter("smita patankar", "a"), "a = 4")

if __name__ == "__main__":
    unittest.main()
