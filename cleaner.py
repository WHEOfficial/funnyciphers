import json
from os import write
from cipher import clean_text
quotes = []

with open("cleaned.json", 'r') as infile:
    data = json.load(infile)
    for quote in data:
        length = len(quote['text'])
        if length >= 80 and length <= 130:
            quotes.append(quote)
    
with open("final3.json", 'w') as outfile:
    json.dump(quotes, outfile)