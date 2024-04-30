import unittest
from unittest.mock import patch
from search_engine.search_engine import main

class TestSearchEngine(unittest.TestCase):
    """
    Test cases for the search engine application.
    """
    @patch('builtins.input')
    @patch('search_engine.search_engine.Indexer')
    @patch('search_engine.search_engine.Searcher')
    @patch('sys.argv', ['search_engine.py', '/path/to/directory'])
    def test_main(self, mock_searcher, mock_indexer, mock_input):
        mock_input.side_effect = ["the cat", ":quit"]
        mock_indexer.return_value.read_files.return_value = {
            "file1.txt": "the quick brown fox jumps over the lazy dog",
            "file2.txt": "the cat in the hat",
            "file3.txt": "dog cat mouse"
        }
        mock_searcher.return_value.search.return_value = [
            ("file2.txt", 100.0),
            ("file1.txt", 50.0),
            ("file3.txt", 50.0)
        ]

        with patch('builtins.print') as mock_print:
            main()

        mock_indexer.return_value.read_files.assert_called_with('/path/to/directory')
        mock_searcher.return_value.search.assert_called_with('the cat', {
            "file1.txt": "the quick brown fox jumps over the lazy dog",
            "file2.txt": "the cat in the hat",
            "file3.txt": "dog cat mouse"
        })
        mock_print.assert_any_call("1. file2.txt: 100.00%")
        mock_print.assert_any_call("2. file1.txt: 50.00%")
        mock_print.assert_any_call("3. file3.txt: 50.00%")

    @patch('builtins.input')
    @patch('search_engine.search_engine.Indexer')
    @patch('search_engine.search_engine.Searcher')
    @patch('sys.argv', ['search_engine.py', '/path/to/directory'])
    def test_main_quit(self, mock_searcher, mock_indexer, mock_input):
        mock_input.side_effect = [":quit"]

        with patch('builtins.print') as mock_print:
            main()

        mock_indexer.return_value.read_files.assert_called_with('/path/to/directory')
        mock_searcher.return_value.search.assert_not_called()
        mock_print.assert_not_called()

    @patch('builtins.input')
    @patch('search_engine.search_engine.Indexer')
    @patch('search_engine.search_engine.Searcher')
    @patch('sys.argv', ['search_engine.py', '/path/to/directory'])
    def test_main_no_results(self, mock_searcher, mock_indexer, mock_input):
        mock_input.side_effect = ["python programming", ":quit"]
        mock_indexer.return_value.read_files.return_value = {
            "file1.txt": "the quick brown fox",
            "file2.txt": "the cat in the hat",
            "file3.txt": "dog cat mouse"
        }
        mock_searcher.return_value.search.return_value = []

        with patch('builtins.print') as mock_print:
            main()

        mock_indexer.return_value.read_files.assert_called_with('/path/to/directory')
        mock_searcher.return_value.search.assert_called_with('python programming', {
            "file1.txt": "the quick brown fox",
            "file2.txt": "the cat in the hat",
            "file3.txt": "dog cat mouse"
        })
        mock_print.assert_not_called()
