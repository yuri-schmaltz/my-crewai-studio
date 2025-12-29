import unittest
from app.my_agent import Agent

class TestAgent(unittest.TestCase):
    def test_agent_creation(self):
        agent = Agent(role="tester", backstory="test", goal="test", allow_delegation=True)
        self.assertEqual(agent.role, "tester")
        self.assertTrue(agent.allow_delegation)

if __name__ == "__main__":
    unittest.main()
