import unittest
from app.result import Result

class TestResult(unittest.TestCase):
    def test_result_init(self):
        result = Result(id="1", crew_name="Crew", result="ok", inputs={}, formatted_result="ok", created_at=None)
        self.assertEqual(result.crew_name, "Crew")
        self.assertEqual(result.result, "ok")

if __name__ == "__main__":
    unittest.main()
