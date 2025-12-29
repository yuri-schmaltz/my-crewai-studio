import unittest
from app.pg_tools import PageTools

class TestPageToolsToolClass(unittest.TestCase):
    def test_tool_class_type(self):
        page = PageTools()
        for tool_name in page.available_tools.keys():
            tool_class = page.available_tools[tool_name]
            self.assertTrue(callable(tool_class))

if __name__ == "__main__":
    unittest.main()
