from ArtGenerator import ArtGenerator
from PoemFetcher import PoemFetcher
from LLMFineTuner import LLMFineTuner

def main():
    # Initialize the PoemFetcher with a source
    poet = "Poet"
    poem_fetcher = PoemFetcher(poet)

    # Fetch poems and prompt-poem pairs
    prompt_poem_pairs = poem_fetcher.fetch_poems()

    # Initialize and fine-tune the LLM with the fetched data
    llm_model = "pretrained-llm-model"  # Replace with actual model
    llm_fine_tuner = LLMFineTuner(llm_model)
    llm_fine_tuner.fine_tune_data = prompt_poem_pairs
    llm_fine_tuner.fine_tune_model()

    # Generate a new poem using a prompt
    prompt = "The beauty of nature"
    generated_poem = llm_fine_tuner.generate_poem(prompt)
    print(f"Generated Poem:\n{generated_poem}")

    # Initialize the ArtGenerator with a style and create visual art from the poem
    art_style = "abstract"
    art_generator = ArtGenerator(art_style)
    visual_art = art_generator.generate_visual_art(generated_poem)
    
    # Display or handle the generated visual art (placeholder)
    print("Visual art created for the poem.")

if __name__ == "__main__":
    main()
