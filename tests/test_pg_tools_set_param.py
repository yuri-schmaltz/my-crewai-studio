import unittest
from app.pg_tools import PageTools

class TestPageToolsSetParam(unittest.TestCase):
    def test_set_tool_parameter_exists(self):
        page = PageTools()
        self.assertTrue(hasattr(page, "set_tool_parameter"))

if __name__ == "__main__":
    unittest.main()
