import unittest
from app.pg_tools import PageTools

class TestPageTools(unittest.TestCase):
    def test_init(self):
        page = PageTools()
        self.assertIsNotNone(page)

if __name__ == "__main__":
    unittest.main()
