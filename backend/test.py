import requests

BASE = "http://127.0.0.1:5000/"

data = [
    {"likes": 125676, "name": "Interstellar", "views": 42367123},
    {"likes": 551356, "name": "Lord of The Rings", "views": 92352671},
    {"likes": 10, "name": "How to make REST API", "views": 21},
]

for i in range(len(data)):
    response = requests.put(
        BASE + "video/" + str(i),
        data[i],
    )
    print(response.json())


input()
response = requests.get(BASE + "video/2")
print(response.json())
