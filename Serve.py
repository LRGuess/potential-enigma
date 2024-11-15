import json

with open('database/riddles.json') as r:
  riddles = json.load(r)

print(riddles)
