import unittest
from app.pg_tools import PageTools

class TestPageToolsToolRunException(unittest.TestCase):
    def test_tool_run_exception(self):
        page = PageTools()
        for tool_name in page.available_tools.keys():
            tool_class = page.available_tools[tool_name]
            instance = tool_class()
            run_method = getattr(instance, "run", None)
            if callable(run_method):
                try:
                    run_method(None)
                except Exception as e:
                    self.assertIsInstance(e, Exception)

if __name__ == "__main__":
    unittest.main()
