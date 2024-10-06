from ArtGenerator import ArtGenerator
from PoemFetcher import PoemFetcher
from MarkovChain import MarkovGenerator

def main():
    poet_name = "Percy Bysshe Shelley"
    poet_name_2= "Emily Dickinson"
    poet_name_3= "Oscar Wilde"
    poet_name_4= "William blake"

    # Create an instance of PoemFetcher
    fetcher = PoemFetcher(poet_name_2)
    #fetcher.fetch_poems()
    filename = f"poems/{poet_name.lower().replace(' ', '_')}_poems.json"
    filename_2 = f"poems/{poet_name_2.lower().replace(' ', '_')}_poems.json"
    filename_3 = f"poems/{poet_name_3.lower().replace(' ', '_')}_poems.json"
    filename_4 = f"poems/{poet_name_4.lower().replace(' ', '_')}_poems.json"
    #fetcher.save_to_file(filename)
    ''''
    fetcher.load_from_file(filename_2, file_format='json')
    fetcher.load_from_file(filename_3, file_format='json')
    fetcher.load_from_file(filename_4, file_format='json')
    '''
    fetcher.load_from_file(filename_2, file_format='json')
    poems= fetcher.get_poems()


    poem_generator= MarkovGenerator(poems, state_size= 1)
    poem= poem_generator.generate_poem()
    #poem_generator.check_plagiarism(poem)
    #print(f"Plagarism Score: {poem_generator.overall_plagiarism_score(poem)}")
    print("Poem:")
    print(poem)
        
if __name__ == "__main__":
    main()
