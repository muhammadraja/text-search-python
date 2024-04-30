import os
import logging

logger = logging.getLogger(__name__)

class Indexer:
    """
    Handles reading files and building an in-memory index.
    """
    def read_files(self, directory):
        """
        Reads all text files in the given directory and returns an in-memory
        index representation of the files and their contents.

        Args:
            directory (str): The path to the directory containing text files.

        Returns:
            dict: A dictionary where the keys are the filenames and the values are
            the contents of the files.
        """
        file_index = {}
        try:
            for filename in os.listdir(directory):
                if filename.endswith(".txt"):
                    file_path = os.path.join(directory, filename)
                    with open(file_path, "r") as file:
                        content = file.read()
                        file_index[filename] = content
                else:
                    logger.warning(f"Skipping non-text file: {filename}")
        except OSError as e:
            logger.error(f"Error reading files from directory '{directory}': {e}")
            return {}
        return file_index
