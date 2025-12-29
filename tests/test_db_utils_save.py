import unittest
from app.db_utils import save_crew

class TestDbUtilsSave(unittest.TestCase):
    def test_save_crew_exists(self):
        self.assertTrue(callable(save_crew))

if __name__ == "__main__":
    unittest.main()
