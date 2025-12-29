import unittest
from app.utils import get_tasks_outputs_str

class TestUtilsGetTasks(unittest.TestCase):
    def test_get_tasks_outputs_str(self):
        result = get_tasks_outputs_str(["output"])
        self.assertIn("output", result)

if __name__ == "__main__":
    unittest.main()
