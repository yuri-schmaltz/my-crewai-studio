import unittest
from app.pg_knowledge import PageKnowledge

class TestPageKnowledge(unittest.TestCase):
    def test_init(self):
        page = PageKnowledge()
        self.assertIsNotNone(page)

if __name__ == "__main__":
    unittest.main()
