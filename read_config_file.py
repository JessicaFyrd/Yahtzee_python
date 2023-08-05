import json

with open("/Users/jess/Documents/Python/Yahtzee/config.json", "r") as jsonfile:
    json_config = json.load(jsonfile)
    print("Read successful")
print(json_config)
print(json_config['nbJoueur'])