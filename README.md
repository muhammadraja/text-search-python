# Simple Text Search Engine | Python

This is a command-line driven text search engine implemented in Python. It reads all the text files in a given directory, builds an in-memory index of the files and their contents, and then allows the user to perform interactive searches.

## Requirements

- Python 3.12.1

## Usage

1. Clone the repository:
   `git clone https://github.com/muhammadraja/text-search-python.git`

2. Navigate to the project directory:
   `cd text-search-python`

3. Install the required dependencies:
   `pip install -r requirements.txt`

4. Run the search engine:
   `python search_engine/search_engine.py </path/to/directory/containing/text/files>`

Replace the path with the path to the files

This will read all the text files in the specified directory and start the interactive search prompt.

5. Enter your search queries at the `search>` prompt. Type `:quit` to exit the program.

## Features

- Reads all text files in a given directory and builds an in-memory index of the file contents.
- Performs case-insensitive searches on the file contents.
- Ranks the search results based on the percentage of matching words in each file.
- Displays the top 10 (or fewer) matching filenames with their relevance scores.
- Provides error handling and logging for various scenarios.

## Testing

To run the unit tests, execute the following command:

`python -m unittest discover tests`

This will run the tests defined in the `tests` directory and display the results.

## Directory Structure

- `search_engine/` is the main directory containing the project code.
  - `__init__.py` initialises the `search_engine` package.
  - `indexer.py` contains code for indexing documents.
  - `searcher.py` contains code for searching documents.
  - `search_engine.py` is the main script for running the search engine.
- `tests/` is the directory containing test files.
  - `__init__.py` initialises the `tests` package.
  - `test_indexer.py` contains tests for the indexer module.
  - `test_searcher.py` contains tests for the searcher module.
  - `test_search_engine.py` contains tests for the search engine script.
- `README.md` is the Markdown file containing project information.
- `requirements.txt` lists the project dependencies.

## Future Improvements

- Implement more advanced ranking algorithms, such as considering the position of the matching words or the overall frequency of the words in the files.
- Add support for more complex search queries, such as boolean operators or phrase matching.
- Implement persistence of the file index to avoid rebuilding it on every run.
- Provide a more user-friendly command-line interface, such as tab completion or history.
- Use the Python libraries like `Whoosh` for this task
