import unittest
from app.my_task import MyTask
from app.db_utils import save_task

class TestIntegrationTask(unittest.TestCase):
    def test_task_save(self):
        task = MyTask(id="1", name="Test", description="desc", expected_output="output")
        try:
            save_task(task)
            success = True
        except Exception:
            success = False
        self.assertTrue(success)

if __name__ == "__main__":
    unittest.main()
