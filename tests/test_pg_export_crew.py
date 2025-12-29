import unittest
from app.pg_export_crew import main

class TestPgExportCrew(unittest.TestCase):
    def test_main_exists(self):
        self.assertTrue(callable(main))

if __name__ == "__main__":
    unittest.main()
