import json
file = open("data.json", "r")
data = json.load(file)
search = input()
if "facebook" in data:
    print(data[search]['email'])

