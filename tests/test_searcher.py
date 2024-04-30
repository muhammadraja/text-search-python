import unittest
from search_engine.searcher import Searcher

class TestSearcher(unittest.TestCase):
    """
    Test cases for the Searcher class.
    """
    def test_search(self):
        file_index = {
            "file1.txt": "the quick brown fox jumps over the lazy dog",
            "file2.txt": "the cat in the hat",
            "file3.txt": "dog cat mouse"
        }

        searcher = Searcher()
        results = searcher.search("the cat", file_index)

        expected_results = [
            ("file2.txt", 100.0),
            ("file1.txt", 50.0),
            ("file3.txt", 50.0)
        ]
        self.assertEqual(results, expected_results)
