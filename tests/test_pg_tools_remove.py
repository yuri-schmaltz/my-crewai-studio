import unittest
from app.pg_tools import PageTools

class TestPageToolsRemove(unittest.TestCase):
    def test_remove_tool_exists(self):
        page = PageTools()
        self.assertTrue(hasattr(page, "remove_tool"))

if __name__ == "__main__":
    unittest.main()
