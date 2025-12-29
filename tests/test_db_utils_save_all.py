import unittest
from app.db_utils import save_crew, save_tool, save_result, save_task, save_knowledge_source

class TestDbUtilsSaveAll(unittest.TestCase):
    def test_all_save_functions_exist(self):
        self.assertTrue(callable(save_crew))
        self.assertTrue(callable(save_tool))
        self.assertTrue(callable(save_result))
        self.assertTrue(callable(save_task))
        self.assertTrue(callable(save_knowledge_source))

if __name__ == "__main__":
    unittest.main()
