import unittest
from app.pg_tools import PageTools

class TestPageToolsDraw(unittest.TestCase):
    def test_draw_exists(self):
        page = PageTools()
        self.assertTrue(hasattr(page, "draw"))

if __name__ == "__main__":
    unittest.main()
