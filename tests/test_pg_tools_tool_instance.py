import unittest
from app.pg_tools import PageTools

class TestPageToolsToolInstance(unittest.TestCase):
    def test_tool_instance_creation(self):
        page = PageTools()
        for tool_name in page.available_tools.keys():
            tool_class = page.available_tools[tool_name]
            instance = tool_class()
            self.assertIsNotNone(instance)

if __name__ == "__main__":
    unittest.main()
