import unittest
from app.pg_crews import PageCrews

class TestPageCrews(unittest.TestCase):
    def test_init(self):
        page = PageCrews()
        self.assertIsNotNone(page)

if __name__ == "__main__":
    unittest.main()
