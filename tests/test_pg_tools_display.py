import unittest
from app.pg_tools import PageTools

class TestPageToolsDisplay(unittest.TestCase):
    def test_draw_tools_exists(self):
        page = PageTools()
        self.assertTrue(hasattr(page, "draw_tools"))

if __name__ == "__main__":
    unittest.main()
