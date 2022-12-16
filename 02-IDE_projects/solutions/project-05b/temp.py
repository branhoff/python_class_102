import json

with open("prize.json", 'r') as infile:
    prize_dict = json.load(infile)

for year in prize_dict["prizes"]:
    year["year"]


print("1933" > "2001")