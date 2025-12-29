import unittest
from app.result import Result
from app.db_utils import save_result

class TestIntegrationResult(unittest.TestCase):
    def test_result_save(self):
        result = Result(id="1", crew_name="Crew", result="ok", inputs={}, formatted_result="ok", created_at=None)
        try:
            save_result(result)
            success = True
        except Exception:
            success = False
        self.assertTrue(success)

if __name__ == "__main__":
    unittest.main()
