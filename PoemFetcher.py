

class PoemFetcher:
    def __init__(self, source: str):
        self.author: str = source
    
    def fetch_poems(self) -> list[tuple[str, str]]:
        """
        Fetches poems from the specified author.
        Returns:
            List of tuples containing prompt-poem pairs.
        """
        # Implementation to fetch poems
        return []


