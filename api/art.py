import requests
import json
from random import randint

def getPaintingURL():
    parameters = {
     "q": "ocean",
     "isHighlight": 'true',
     "medium": 'Paintings',
     "hasImages": 'true'
    }

    response = requests.get(
        "https://collectionapi.metmuseum.org/public/collection/v1/search", params=parameters).json()

    if int(response['total']) != 0:
        objectId = response['objectIDs'][randint(0, int(response['total']) - 1)]
        reply = requests.get(
            "https://collectionapi.metmuseum.org/public/collection/v1/objects/{}".format(str(objectId)))
        return reply.json()['primaryImage']