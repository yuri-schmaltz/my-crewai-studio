import unittest
from app.tools.CustomCodeInterpreterTool import CustomCodeInterpreterTool

class TestCustomCodeInterpreterTool(unittest.TestCase):
    def test_init(self):
        tool = CustomCodeInterpreterTool(workspace_dir="/tmp")
        self.assertEqual(tool.workspace_dir, "/tmp")

if __name__ == "__main__":
    unittest.main()
