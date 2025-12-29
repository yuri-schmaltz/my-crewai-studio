import unittest
from app.my_crew import MyCrew
from app.db_utils import save_crew

class TestIntegrationCrewSave(unittest.TestCase):
    def test_crew_save(self):
        crew = MyCrew(name="TestCrew", manager_llm=None, tasks=[], knowledge_source_ids=[])
        try:
            save_crew(crew)
            success = True
        except Exception:
            success = False
        self.assertTrue(success)

if __name__ == "__main__":
    unittest.main()
