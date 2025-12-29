import unittest
from app.my_agent import Agent
from app.my_crew import MyCrew
from app.my_task import MyTask
from app.db_utils import save_crew, save_task, save_result
from app.result import Result

class TestIntegrationFullFlow(unittest.TestCase):
    def test_full_flow(self):
        agent = Agent(role="tester", backstory="test", goal="test", allow_delegation=True)
        crew = MyCrew(name="TestCrew", manager_llm=agent, tasks=[], knowledge_source_ids=[])
        save_crew(crew)
        task = MyTask(id="1", name="Test", description="desc", expected_output="output")
        save_task(task)
        result = Result(id="1", crew_name=crew.name, result="ok", inputs={}, formatted_result="ok", created_at=None)
        save_result(result)
        self.assertEqual(result.crew_name, "TestCrew")
        self.assertEqual(result.result, "ok")

if __name__ == "__main__":
    unittest.main()
