import unittest
from app.db_utils import save_tool

class TestDbUtilsSaveTool(unittest.TestCase):
    def test_save_tool_exists(self):
        self.assertTrue(callable(save_tool))

if __name__ == "__main__":
    unittest.main()
