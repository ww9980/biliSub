import json

output = open("out.txt", "a", encoding="utf8")

with open('in.json', encoding="utf8") as f:
    data = json.load(f)
    for i in data['body']:
        output.write(i['content'] + "\n")
output.close()
