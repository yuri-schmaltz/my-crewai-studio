import unittest
from app.my_knowledge_source import MyKnowledgeSource
from app.db_utils import save_knowledge_source

class TestIntegrationKnowledge(unittest.TestCase):
    def test_knowledge_save(self):
        ks = MyKnowledgeSource(id="ks1", name="KS", description="desc")
        try:
            save_knowledge_source(ks)
            success = True
        except Exception:
            success = False
        self.assertTrue(success)

if __name__ == "__main__":
    unittest.main()
