import unittest
from app.pg_tools import PageTools

class TestPageToolsToolRun(unittest.TestCase):
    def test_tool_run_callable(self):
        page = PageTools()
        for tool_name in page.available_tools.keys():
            tool_class = page.available_tools[tool_name]
            instance = tool_class()
            self.assertTrue(callable(getattr(instance, "run", None)))

if __name__ == "__main__":
    unittest.main()
