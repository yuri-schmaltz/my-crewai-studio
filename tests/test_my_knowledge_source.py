import unittest
from app.my_knowledge_source import MyKnowledgeSource

class TestMyKnowledgeSource(unittest.TestCase):
    def test_init(self):
        ks = MyKnowledgeSource(id="ks1", name="KS", description="desc")
        self.assertEqual(ks.name, "KS")
        self.assertEqual(ks.description, "desc")

if __name__ == "__main__":
    unittest.main()
