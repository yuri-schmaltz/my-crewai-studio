import unittest
from app.my_tools import TOOL_CLASSES
from app.db_utils import save_tool

class TestIntegrationToolSave(unittest.TestCase):
    def test_tool_save(self):
        for tool_class in TOOL_CLASSES:
            try:
                tool = tool_class()
                save_tool(tool)
                success = True
            except Exception:
                success = False
            self.assertTrue(success)

if __name__ == "__main__":
    unittest.main()
