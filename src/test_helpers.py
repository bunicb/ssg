import unittest
from helpers import extract_title

class HelpersTestCase(unittest.TestCase):
    def test_extract_title(self):
        md = """
# This is a title
This is a paragraph with some text.
"""
        expected_title = "This is a title"
        self.assertEqual(extract_title(md), expected_title)

    def test_extract_title_no_title(self):
        md = """
This is a paragraph with some text.
"""
        self.assertRaises(Exception, extract_title, md)

if __name__ == "__main__":
    unittest.main()