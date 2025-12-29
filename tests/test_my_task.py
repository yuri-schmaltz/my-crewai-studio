import unittest
from app.my_task import MyTask

class TestMyTask(unittest.TestCase):
    def test_init(self):
        task = MyTask(id="1", name="Test", description="desc", expected_output="output")
        self.assertEqual(task.name, "Test")
        self.assertEqual(task.expected_output, "output")

if __name__ == "__main__":
    unittest.main()
