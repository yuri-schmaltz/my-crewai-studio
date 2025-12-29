import unittest
from app.tools.CustomApiTool import CustomApiTool

class TestCustomApiTool(unittest.TestCase):
    def test_run_timeout(self):
        tool = CustomApiTool(base_url="http://localhost", headers={}, query_params={})
        result = tool._run(endpoint="test", method="GET")
        self.assertIn("status_code", result)
        self.assertTrue(result["status_code"] in [200, 500])

if __name__ == "__main__":
    unittest.main()
