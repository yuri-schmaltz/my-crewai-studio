import unittest
from app.pg_results import PageResults

class TestPageResults(unittest.TestCase):
    def test_init(self):
        page = PageResults()
        self.assertIsNotNone(page)

if __name__ == "__main__":
    unittest.main()
