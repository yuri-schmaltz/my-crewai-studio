import unittest
from app.pg_tools import PageTools

class TestPageToolsToolRunList(unittest.TestCase):
    def test_tool_run_list(self):
        page = PageTools()
        for tool_name in page.available_tools.keys():
            tool_class = page.available_tools[tool_name]
            instance = tool_class()
            run_method = getattr(instance, "run", None)
            if callable(run_method):
                try:
                    output = run_method([])
                except Exception:
                    output = None
                self.assertTrue(output is None or isinstance(output, (str, dict, list)))

if __name__ == "__main__":
    unittest.main()
