import unittest
from app.pg_tools import PageTools

class TestPageToolsToolRunArgs(unittest.TestCase):
    def test_tool_run_args(self):
        page = PageTools()
        for tool_name in page.available_tools.keys():
            tool_class = page.available_tools[tool_name]
            instance = tool_class()
            run_method = getattr(instance, "run", None)
            self.assertIsNotNone(run_method)
            self.assertTrue(callable(run_method))

if __name__ == "__main__":
    unittest.main()
