import unittest
from app.db_utils import save_task

class TestDbUtilsSaveTask(unittest.TestCase):
    def test_save_task_exists(self):
        self.assertTrue(callable(save_task))

if __name__ == "__main__":
    unittest.main()
