import requests

BASE = "http://127.0.0.1:5000/"

data = [
    {"name": "Interstellar", "views": 42367123, "likes": 125676},
    {"name": "Lord of The Rings", "views": 92352671, "likes": 551356},
    {"name": "How to make REST API", "views": 21, "likes": 10},
]

for i in range(len(data)):
    response = requests.put(
        BASE + f"video/{i}",
        data[i],
    )
    print(response.json())

input()

response = requests.delete(BASE + "video/0")
print(response)

input()

response = requests.get(BASE + "video/2")
print(response.json())
