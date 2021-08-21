import json
from difflib import get_close_matches

def loadJSON():
    data = json.load(open("data.json"))
    return data

def find(key):
    data = loadJSON()
    key = key.lower()
    if key in data:
        return output(data[key])
    elif len(get_close_matches(key, data.keys())) > 0:
        key = get_close_matches(key, data.keys(),n=1)[0]
        print("Did you mean {} instead".format(key))
        user = input("Would you like to try this {}? Y/N ".format(key))
        if user == 'y' or 'Y':
            return output(data[key])
        else:
            return print("This word does not exist. Please double check it.")
    else:
        return print("This word does not exist. Please double check it.")

def output(definition):
    print(definition)

