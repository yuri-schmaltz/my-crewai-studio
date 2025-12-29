import unittest
from app.my_agent import Agent
from app.my_crew import MyCrew

class TestIntegrationAgentCrew(unittest.TestCase):
    def test_agent_crew_integration(self):
        agent = Agent(role="tester", backstory="test", goal="test", allow_delegation=True)
        crew = MyCrew(name="TestCrew", manager_llm=None, tasks=[], knowledge_source_ids=[])
        self.assertEqual(agent.role, "tester")
        self.assertEqual(crew.name, "TestCrew")
        # Simula integração básica
        crew.manager_llm = agent
        self.assertIs(crew.manager_llm, agent)

if __name__ == "__main__":
    unittest.main()
