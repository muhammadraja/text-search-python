import unittest
from unittest.mock import patch
from search_engine.indexer import Indexer

class TestIndexer(unittest.TestCase):
    """
    Tests for the File Indexing class.
    """
    @patch('os.listdir')
    @patch('builtins.open')
    def test_read_files(self, mock_open, mock_listdir):
        mock_listdir.return_value = ['file1.txt', 'file2.txt', 'file3.txt']
        mock_open.return_value.__enter__.return_value.read.side_effect = ['content1', 'content2', 'content3']

        indexer = Indexer()
        file_index = indexer.read_files('/path/to/directory')

        self.assertEqual(file_index, {
            'file1.txt': 'content1',
            'file2.txt': 'content2',
            'file3.txt': 'content3'
        })
