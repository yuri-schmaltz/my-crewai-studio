import unittest
from app.utils import format_result

class TestUtilsFormat(unittest.TestCase):
    def test_format_result(self):
        result = format_result({"output": "ok"})
        self.assertIn("ok", result)

if __name__ == "__main__":
    unittest.main()
