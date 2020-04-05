import requests
import json


def writeInFile(file, dataJson):
    with open(file, 'w') as f:
        json.dump(dataJson, f)


def getNYTData():
    return requests.get("https://api.nytimes.com/svc/topstories/v2/home.json", params={"api-key": 'YihnGvBbKB0Wb4tGafCJEI1IrRR3Az9c'}).json()


def changeFormat(dic):
    newDic = {}
    newDic.update({"status": "ok", "totalResults": len(
        dic["results"]), "articles": []})
    print(newDic.get("totalResults"))
    for a in dic["results"]:
        art = {}
        source = {"id": "nyt", "name": "Ney York Times"}
        art.update({"source": source, "author": a["byline"], "title": a["title"], "description": a["abstract"],
                    "url": a["url"], "urlToImage": a["multimedia"][0]["url"], "publishedAt": a["published_date"], "content": ""})
        newDic["articles"].append(art)
    return newDic


data = getData()
writeInFile("initimes.json", data)
data = changeFormat(data)
writeInFile("times.json", data)
