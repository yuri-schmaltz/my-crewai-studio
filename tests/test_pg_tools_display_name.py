import unittest
from app.pg_tools import PageTools

class TestPageToolsDisplayName(unittest.TestCase):
    def test_get_tool_display_name_exists(self):
        page = PageTools()
        self.assertTrue(hasattr(page, "get_tool_display_name"))

if __name__ == "__main__":
    unittest.main()
