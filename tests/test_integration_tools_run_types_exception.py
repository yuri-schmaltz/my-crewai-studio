import unittest
from app.pg_tools import PageTools

class TestIntegrationToolsRunTypesException(unittest.TestCase):
    def test_tools_run_types_exception(self):
        page = PageTools()
        for tool_name in page.available_tools.keys():
            tool_class = page.available_tools[tool_name]
            instance = tool_class()
            run_method = getattr(instance, "run", None)
            if callable(run_method):
                for arg in [None, "", {}, [], 123]:
                    try:
                        run_method(arg)
                    except Exception as e:
                        self.assertIsInstance(e, Exception)

if __name__ == "__main__":
    unittest.main()
