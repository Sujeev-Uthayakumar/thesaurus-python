import json

def loadJSON():
    data = json.load(open("data.json"))
    return data

def find(key):
    data = loadJSON()
    key = key.lower()
    if key in data:
        return output(data[key])
    else:
        return print("This word does not exist")

def output(definition):
    print(definition)

