import unittest
import sys
import os

# Add project root directory to system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utilities.fetch import get_summary


class TestWikipediaSummary(unittest.TestCase):

    def test_valid_topic(self):
        """Test fetching summary of a valid Wikipedia topic."""
        summary = get_summary("Python programming", sentences=2)
        self.assertTrue(len(summary) > 0, "Summary should not be empty for a valid topic.")

    def test_invalid_topic(self):
        """Test fetching summary of an invalid Wikipedia topic."""
        summary = get_summary("asjdkflasjdfkl", sentences=2)
        self.assertTrue("Could not fetch data" in summary or "No summary found" in summary)

    def test_disambiguation_topic(self):
        """Test fetching a disambiguation topic (like Mercury)."""
        summary = get_summary("Mercury", sentences=2)
        self.assertTrue(len(summary) > 0, "Disambiguation page should return some text.")

if __name__ == "__main__":
    unittest.main()
