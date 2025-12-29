import unittest
from app.pg_tools import PageTools

class TestIntegrationToolsRunTypesList(unittest.TestCase):
    def test_tools_run_types_list(self):
        page = PageTools()
        for tool_name in page.available_tools.keys():
            tool_class = page.available_tools[tool_name]
            instance = tool_class()
            run_method = getattr(instance, "run", None)
            if callable(run_method):
                output = None
                try:
                    output = run_method([])
                except Exception:
                    pass
                self.assertTrue(output is None or isinstance(output, (str, dict, list)))

if __name__ == "__main__":
    unittest.main()
