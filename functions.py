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
        if user == 'Y' or user == 'y':
            return output(data[key])
        elif user == 'N' or user == 'n':
            return print("This word does not exist. Please double check it.")
        else:
            return print("The entry cannot be understood!")
    else:
        return print("This word does not exist. Please double check it.")

def output(definitions):
    count = 0
    print("Definitions:")
    for definition in definitions:
        count = count + 1
        print("{0}: {1}".format(count, definition))

