import unittest
from app.pg_tools import PageTools

class TestPageToolsAvailable(unittest.TestCase):
    def test_available_tools_exists(self):
        page = PageTools()
        self.assertTrue(hasattr(page, "available_tools"))

if __name__ == "__main__":
    unittest.main()
