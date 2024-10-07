import requests
import json
import yaml
import re
from collections import Counter
import os

class PoemFetcher:
    def __init__(self, poet_name):
        self.poet_name = poet_name
        self.poems = []
        self.stats = {}

    def fetch_poems(self):
        url = f"https://poetrydb.org/author/{self.poet_name}"
        response = requests.get(url)
        if response.status_code == 200:
            self.poems = response.json()
            # Check if the response is valid
            if isinstance(self.poems, list) and len(self.poems) > 0 and isinstance(self.poems[0], dict):
                print(f"Successfully fetched {len(self.poems)} poems by {self.poet_name}.")
            else:
                print(f"Error: No poems found for {self.poet_name}.")
                self.poems = []
        else:
            print(f"Error: Unable to fetch poems (Status code: {response.status_code})")
            self.poems = []

    def compute_statistics(self):
        if not self.poems:
            print("No poems available to compute statistics.")
            return

        num_poems = len(self.poems)
        total_words = 0
        word_counter = Counter()

        for poem in self.poems:
            poem_text = " ".join(poem['lines'])
            words = re.findall(r'\b\w+\b', poem_text.lower())
            total_words += len(words)
            word_counter.update(words)

        mean_length = total_words / num_poems if num_poems > 0 else 0
        num_unique_words = len(word_counter)

        self.stats = {
            'number_of_poems': num_poems,
            'mean_length_of_poems': mean_length,
            'number_of_unique_words': num_unique_words
        }

    def save_to_file(self, filename, file_format='json'):
        data = {
            'poems': self.poems,
            'statistics': self.stats
        }

        if file_format == 'json':
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            print(f"Data saved to {filename} in JSON format.")
        elif file_format == 'yaml':
            with open(filename, 'w', encoding='utf-8') as f:
                yaml.dump(data, f, allow_unicode=True)
            print(f"Data saved to {filename} in YAML format.")
        else:
            print(f"Error: Unsupported file format '{file_format}'. Please use 'json' or 'yaml'.")

    def load_from_file(self, filename, file_format='json'):
        # If file exists, load and aggregate data
        if not os.path.exists(filename):
            print(f"Error: File {filename} does not exist.")
            return

        try:
            with open(filename, 'r', encoding='utf-8') as f:
                if file_format == 'json':
                    data = json.load(f)
                elif file_format == 'yaml':
                    data = yaml.safe_load(f)
                else:
                    print(f"Error: Unsupported file format '{file_format}'. Please use 'json' or 'yaml'.")
                    return
            
            # Aggregate poems
            new_poems = data.get('poems', [])
            self.poems.extend(new_poems)
            print(f"Loaded {len(new_poems)} poems from {filename}.")
            
            # Recompute statistics to include new data
            self.compute_statistics()
        except Exception as e:
            print(f"Error loading data from file: {e}")

    def get_poems(self):
        return self.poems
