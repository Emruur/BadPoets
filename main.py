import os
from PoemFetcher import PoemFetcher
from MarkovChain import MarkovGenerator

class BadPoets:
    def __init__(self, poets):
        # Convert single poet input to a list
        if isinstance(poets, str):
            poets = [poets]
        self.poets = poets
        self.poems = []
        self.failed_poets = []
        self.load_or_fetch_poems()

    def load_or_fetch_poems(self):
        # Ensure the poems directory exists
        os.makedirs("poems", exist_ok=True)

        for poet in self.poets:
            filename = f"poems/{poet.lower().replace(' ', '_')}_poems.json"
            fetcher = PoemFetcher(poet)

            try:
                # Check if the poem file exists
                if os.path.exists(filename):
                    fetcher.load_from_file(filename, file_format='json')
                else:
                    # Attempt to fetch poems
                    fetcher.fetch_poems()
                    fetcher.save_to_file(filename)
                    fetcher.load_from_file(filename)
                
            except Exception as e:
                # If fetching/loading fails, record the poet name
                self.failed_poets.append(poet)
                print(f"Failed to fetch or load poems for {poet}: {str(e)}")
        self.poems= fetcher.get_poems()

    def generate_poem(self, state_size=2):
        if not self.poems:
            raise ValueError("No poems available to generate from. Check if the poets were correctly fetched.")
        
        # Generate a poem using Markov chains
        poem_generator = MarkovGenerator(self.poems, state_size=state_size)
        poem = poem_generator.generate_poem()

        poem_generator.check_plagiarism(poem)
        return poem

# Usage
if __name__ == "__main__":
    # Example poets list
    poets = ["Emily Dickinson", "NonExistent Poet", "William Blake"]
    poets= "Emily Dickinson"

    # Create an instance of BadPoets
    bad_poets = BadPoets(poets)

    # Check for failed poets
    if bad_poets.failed_poets:
        print("Failed to fetch poems for the following poets:")
        print(", ".join(bad_poets.failed_poets))

    # Generate a poem if any poems were successfully loaded/fetched
    try:
        poem = bad_poets.generate_poem()
        print()
        print("Generated Poem:")
        print(poem)
    except ValueError as ve:
        print(ve)
