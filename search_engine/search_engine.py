import argparse
import logging

from indexer import Indexer
from searcher import Searcher

logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')
logger = logging.getLogger(__name__)

def main():
    """
    The main entry point of the search engine application powered by MTRaja.

    This function handles the command-line arguments, reads the files, and performs the search.

    Only supports *.txt files for now.
    """
    parser = argparse.ArgumentParser(description="Simple text search engine powered by MTRaja")
    parser.add_argument("directory", help="Path to the directory containing text files")
    args = parser.parse_args()

    indexer = Indexer()
    try:
        file_index = indexer.read_files(args.directory)
        logger.info(f"{len(file_index)} files read in directory {args.directory}")
    except Exception as e:
        logger.error(f"Error reading files from directory '{args.directory}': {e}")
        return

    searcher = Searcher()
    while True:
        query = input("search> ")
        if query.strip() == ":quit":
            break
        try:
            results = searcher.search(query, file_index)
            for i, (filename, score) in enumerate(results):
                print(f"{i+1}. {filename}: {score:.2f}%")
        except Exception as e:
            logger.error(f"Error performing search: {e}")

if __name__ == "__main__":
    main()
