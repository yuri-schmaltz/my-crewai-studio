import unittest
import os
from app.tools.ScrapflyScrapeWebsiteTool import ScrapflyScrapeWebsiteTool

class TestScrapflyScrapeWebsiteTool(unittest.TestCase):
    def test_init_env(self):
        os.environ["SCRAPFLY_API_KEY"] = "dummy_key"
        tool = ScrapflyScrapeWebsiteTool()
        self.assertEqual(tool.api_key, "dummy_key")

if __name__ == "__main__":
    unittest.main()
