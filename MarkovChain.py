import markovify
import difflib

class MarkovGenerator:
    def __init__(self, poems, state_size=1):
        # Combine all poems into one text for training
        self.text = "\n".join(line for poem in poems for line in poem["lines"])
        self.original_lines = [line for poem in poems for line in poem["lines"]]
        self.model = markovify.Text(self.text, state_size=state_size)
    
    def generate_poem(self, length=3, start=None, strict=False):
        poem_lines = []
        for _ in range(length):
            if start:
                line = self.model.make_sentence_with_start(start, strict=strict)
                start = None  # Use start only for the first line
            else:
                line = self.model.make_sentence(tries=100)
            if line:
                poem_lines.append(line)
        
        return "\n".join(poem_lines)
    
    def check_plagiarism(self, generated_poem, similarity_threshold=0.5):
        plagiarized_lines = []
        # Split generated poem into lines
        generated_lines = generated_poem.split("\n")
        
        for gen_line in generated_lines:
            # Compare each generated line against the original lines
            for orig_line in self.original_lines:
                # Calculate similarity ratio
                similarity = difflib.SequenceMatcher(None, gen_line, orig_line).ratio()
                if similarity >= similarity_threshold:
                    plagiarized_lines.append((gen_line, orig_line, similarity))
                    break  # Stop checking once a similar line is found
        
        return plagiarized_lines
