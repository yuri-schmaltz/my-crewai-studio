import unittest
from app.db_utils import save_result

class TestDbUtilsSaveResult(unittest.TestCase):
    def test_save_result_exists(self):
        self.assertTrue(callable(save_result))

if __name__ == "__main__":
    unittest.main()
