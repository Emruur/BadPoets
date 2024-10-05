from ArtGenerator import ArtGenerator
from PoemFetcher import PoemFetcher
from MarkovChain import MarkovGenerator

def main():
    poet_name = "Emily Dickinson"

    # Create an instance of PoemFetcher
    fetcher = PoemFetcher(poet_name)
    filename = f"poems/{poet_name.lower().replace(' ', '_')}_poems.json"
    fetcher.load_from_file(filename, file_format='json')
    poems= fetcher.get_poems()

    poem_generator= MarkovGenerator(poems, state_size= 3)
    poem= poem_generator.generate_poem()
    print(poem)

if __name__ == "__main__":
    main()
