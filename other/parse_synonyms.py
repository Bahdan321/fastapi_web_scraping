import requests

def get_synonyms(word, count):
    url = f'https://api.datamuse.com/words?rel_syn={word}&max={count}'
    response = requests.get(url)
    data = response.json()
    synonyms = [entry['word'] for entry in data]
    return synonyms, url
