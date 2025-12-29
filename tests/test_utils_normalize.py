import unittest
from app.utils import normalize_list_indentation

class TestUtilsNormalize(unittest.TestCase):
    def test_normalize(self):
        md = "  * item"
        result = normalize_list_indentation(md)
        self.assertIn("* item", result)

if __name__ == "__main__":
    unittest.main()
