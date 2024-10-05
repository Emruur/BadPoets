import requests

# Define the base URL for the poetrydb API
base_url = "https://poetrydb.org"

# Fetch the list of available poets
response = requests.get(f"{base_url}/author")
if response.status_code == 200:
    poets_data = response.json()
else:
    print("Failed to fetch poets data")
    poets_data = {"authors": []}

# Create a dictionary to store the count of poems for each poet
poets_poem_count = {}

# Iterate over each poet and get the number of poems they have
for poet in poets_data["authors"]:
    poet_response = requests.get(f"{base_url}/author/{poet}")
    if poet_response.status_code == 200:
        poems = poet_response.json()
        poets_poem_count[poet] = len(poems)
    else:
        poets_poem_count[poet] = 0

# Sort poets by the number of poems they have
poets_poem_count_sorted = dict(sorted(poets_poem_count.items(), key=lambda x: x[1], reverse=True))

# Print the poets and their number of poems
for poet, count in poets_poem_count_sorted.items():
    print(f"{poet}: {count} poems")
