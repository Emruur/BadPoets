import markovify

class MarkovGenerator:
    def __init__(self, poems, state_size=1):
        # Combine all poems into one text for training
        self.text = "\n".join(line for poem in poems for line in poem["lines"])
        self.model = markovify.Text(self.text, state_size=state_size)
    
    def generate_poem(self, length=3, start=None, strict=False):
        poem_lines = []
        for _ in range(length):
            if start:
                line = self.model.make_sentence_with_start(start, strict=strict)
                start = None  # Use start only for the first line
            else:
                line = self.model.make_sentence()
            if line:
                poem_lines.append(line)
        
        return "\n".join(poem_lines)