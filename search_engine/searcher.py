import re
import logging

logger = logging.getLogger(__name__)

class Searcher:
    """
    Handles querying the indexed data and ranking results.
    """
    def search(self, query, file_index):
        """
        Searches the file index for the given query and returns the top 10 (or fewer)
        matching filenames with their relevance scores.

        Args:
            query (str): The search query.
            file_index (dict): The in-memory representation of the files and their contents.

        Returns:
            list: A list of tuples, where each tuple contains the filename and the relevance score.
        """
        try:
            # Tokenise the search query and get the unique words
            tokens = re.split(r'\W+', query.lower())
            unique_words = set(tokens)
            total_unique_words = len(unique_words)

            # Initialise a dictionary to store the match counts and relevance scores for each file
            match_counts = {}
            relevance_scores = {}
            for filename, content in file_index.items():
                content_words = set(re.findall(r'\w+', content.lower()))
                matching_words = unique_words.intersection(content_words)
                match_counts[filename] = len(matching_words)
                relevance_scores[filename] = (match_counts[filename] / total_unique_words) * 100

            # Sort the results by relevance score in descending order
            sorted_results = sorted(relevance_scores.items(), key=lambda x: x[1], reverse=True)

            # Return the top 10 (or fewer) results
            return [(filename, score) for filename, score in sorted_results][:10]
        except Exception as e:
            logger.error(f"Error searching the file index: {e}")
            return []
