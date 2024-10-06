import markovify
import difflib

class MarkovGenerator:
    def __init__(self, poems, state_size=1):
        # Combine all poems into one text for training
        if False:
            self.text = "\n".join(line for poem in poems for line in poem["lines"])
            self.model = markovify.Text(self.text, state_size=state_size)
        else:
            print("2222222222222222")
            self.text = "\n".join(line for poem in poems for line in poem["lines"])
            self.model = markovify.NewlineText(self.text, state_size=state_size)

        # Store the original poems as whole strings for plagiarism checking
        self.original_poems = [{"title": poem["title"], "text": " ".join(poem["lines"])} for poem in poems]

    def generate_poem(self, length=3, start=None, strict=False):
        poem_lines = []
        for _ in range(length):
            if start:
                line = self.model.make_sentence_with_start(start, strict=strict)
                start = None  # Use start only for the first line
            else:
                if True:
                    line= self.model.make_sentence()
                else:
                    line = self.model.make_sentence(
                        tries=20000,
                        max_overlap_ratio=1,  # Allow only up to 50% overlap
                        max_overlap_total=3   # Allow overlap of up to 10 words
                    )
            if line:
                poem_lines.append(line)
        
        return "\n".join(poem_lines)  # Concatenate lines to form a full poem
    
    def check_plagiarism(self, generated_poem, ngram_size=5, similarity_threshold=0.8):
        plagiarized_sections = []
        generated_words = generated_poem.split()
        
        # Check n-grams against each original poem
        for i in range(len(generated_words) - ngram_size + 1):
            gen_ngram = " ".join(generated_words[i:i + ngram_size])
            
            # Compare each n-gram to the entire text of each original poem
            for orig_poem in self.original_poems:
                orig_words = orig_poem["text"].split()
                # Check n-grams within the original poem text
                for j in range(len(orig_words) - ngram_size + 1):
                    orig_ngram = " ".join(orig_words[j:j + ngram_size])
                    # Calculate similarity ratio for each n-gram pair
                    similarity = difflib.SequenceMatcher(None, gen_ngram, orig_ngram).ratio()
                    if similarity >= similarity_threshold:
                        plagiarized_sections.append(
                            (gen_ngram, orig_ngram, orig_poem["title"], similarity)
                        )
                        break  # Stop checking further n-grams for this gen_ngram
                # Move to the next n-gram if plagiarism is found
                if plagiarized_sections and plagiarized_sections[-1][0] == gen_ngram:
                    break
     # Print results
        if plagiarized_sections:
            print("Potential plagiarism detected:")
            for gen_ngram, orig_ngram, title, sim in plagiarized_sections:
                print(f"\nGenerated Section: '{gen_ngram}'\nOriginal Section:  '{orig_ngram}'\nTitle of Original Poem: '{title}'\nSimilarity: {sim:.2f}")
        else:
            print("No plagiarism detected.")

    def calculate_similarity(self, text1, text2):
        """Calculate similarity score between two texts."""
        matcher = difflib.SequenceMatcher(None, text1, text2)
        return matcher.ratio()

    def overall_plagiarism_score(self, generated_poem):
        total_similarity = 0
        
        # Compare the generated poem to all original poems and calculate the average similarity
        for orig_poem in self.original_poems:
            similarity = self.calculate_similarity(generated_poem, orig_poem["text"])
            total_similarity += similarity
        
        # Average similarity score
        overall_score = total_similarity / len(self.original_poems)
        
        return overall_score

       