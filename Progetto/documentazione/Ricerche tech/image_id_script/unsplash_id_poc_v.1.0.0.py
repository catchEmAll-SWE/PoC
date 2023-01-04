import requests as rq
import json

ACECSS_KEY = "1CoGBz63unkif-f4iBuOzL4g6o2oP-OMmFoMs7quj24"
valuableWords = ['ferrari', 'apple', 'sunrise', 'banana', 'porche', 'ktm']

for i in valuableWords:
    r = rq.get(
        'https://api.unsplash.com/photos/random/?w=800&h=800&query={0}&client_id={1}'.format(i, ACECSS_KEY))
    jsonContent = json.loads(r.content)
    # print(jsonContent)
    # print("\n")
    print(jsonContent["id"])
