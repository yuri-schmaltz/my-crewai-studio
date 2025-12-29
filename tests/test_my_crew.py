import unittest
from app.my_crew import MyCrew

class TestMyCrew(unittest.TestCase):
    def test_crew_init(self):
        crew = MyCrew(name="TestCrew", manager_llm=None, tasks=[], knowledge_source_ids=[])
        self.assertEqual(crew.name, "TestCrew")
        self.assertEqual(crew.tasks, [])

if __name__ == "__main__":
    unittest.main()
