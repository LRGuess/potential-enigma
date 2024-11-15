import json

# Database url. It will later fetch from this to always have an updated databse to grab from
url = "https://raw.githubusercontent.com/LRGuess/potential-enigma/main/database/riddles.json"

with open('database/riddles.json') as r:
  riddles = json.load(r)

print(riddles)
