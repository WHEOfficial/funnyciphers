import json

with open('data/newquotes.json', 'r') as infile:
    data = json.load(infile)
    total = 0
    for q in data:
        if q['chiSquared'] < 31:
            total += 1
    
    print(total)