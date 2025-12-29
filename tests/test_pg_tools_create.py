import unittest
from app.pg_tools import PageTools

class TestPageToolsCreate(unittest.TestCase):
    def test_create_tool_exists(self):
        page = PageTools()
        self.assertTrue(hasattr(page, "create_tool"))

if __name__ == "__main__":
    unittest.main()
