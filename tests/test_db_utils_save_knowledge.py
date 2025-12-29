import unittest
from app.db_utils import save_knowledge_source

class TestDbUtilsSaveKnowledge(unittest.TestCase):
    def test_save_knowledge_source_exists(self):
        self.assertTrue(callable(save_knowledge_source))

if __name__ == "__main__":
    unittest.main()
