import unittest
from app.utils import generate_printable_view

class TestUtilsGenerate(unittest.TestCase):
    def test_generate_printable_view(self):
        html = generate_printable_view("Crew", "ok", {}, "ok")
        self.assertIn("Crew", html)
        self.assertIn("ok", html)

if __name__ == "__main__":
    unittest.main()
