import unittest
from app.pg_tasks import PageTasks

class TestPageTasks(unittest.TestCase):
    def test_init(self):
        page = PageTasks()
        self.assertIsNotNone(page)

if __name__ == "__main__":
    unittest.main()
