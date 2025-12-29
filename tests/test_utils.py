import unittest
from app.utils import rnd_id, escape_quotes

class TestUtils(unittest.TestCase):
    def test_rnd_id_length(self):
        self.assertEqual(len(rnd_id(10)), 10)
    def test_escape_quotes(self):
        self.assertEqual(escape_quotes('"test"'), '\"test\"')

if __name__ == "__main__":
    unittest.main()
