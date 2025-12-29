import unittest
from app.pg_tools import PageTools

class TestPageToolsDescription(unittest.TestCase):
    def test_tool_description(self):
        page = PageTools()
        for tool_name in page.available_tools.keys():
            tool_class = page.available_tools[tool_name]
            self.assertTrue(hasattr(tool_class, "description"))

if __name__ == "__main__":
    unittest.main()
