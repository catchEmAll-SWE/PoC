import requests as rq
import json
import os

ACCESS_KEY = "1CoGBz63unkif-f4iBuOzL4g6o2oP-OMmFoMs7quj24"
valuableWord = "ship"


os.chdir("../File_Json")

for i in range(5):
    r = rq.get(
          'https://api.unsplash.com/photos/random/?w=200&h=200&query={0}&client_id={1}'.format(valuableWord, ACCESS_KEY))
    jsonContent = json.loads(r.content)
    image = {"id": jsonContent["id"], "class": valuableWord, "reliability": 0}
    json_image = json.dumps(image, indent=3)
    with open("images.json", "a") as f:
        f.write(json_image)
    f.close