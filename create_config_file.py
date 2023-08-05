import json

config_infos = {
    "nbJoueur" : "2"
}

with open("/Users/jess/Documents/Python/Yahtzee/config.json", "w") as jsonfile:
     json.dump(config_infos, jsonfile)