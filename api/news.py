from newsapi import NewsApiClient
from random import randrange
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import json
import time
import sys

app = Flask(__name__)
CORS(app)

## CONSTANTES ##
API_KEY = "f0a443efaaec4868978a2e693c779496"
NYT_KEY = "YihnGvBbKB0Wb4tGafCJEI1IrRR3Az9c"
MOTS_CORONA = ["corona", "covid", "covid-19", "coronavirus",
               "confinement", "quarantaine", "quinzaine", "wuhan", "lockdown", "quarantine", "face mask", "virus"]

UNWANTED_SOURCES_ID = ["hacker-news"]

MAX_PAGE_SIZE = 100

ERR_DIC = {"error": "an error has occured"}

GOOGLE_CATEGORY = ["business",  "entertainment",
                   "general", "health", "science", "sports", "technology"]
NYT_CATEGORY = ["arts", "automobiles", "books", "business", "fashion", "food", "health", "home", "insider", "magazine", "movies", "nyregion", "obituaries",
                "opinion", "politics", "realestate", "science", "sports", "sundayreview", "technology", "theater", "t-magazine", "travel", "upshot", "us", "world"]


## METHODES ##

def removeEmptyEntries(newsDictionary):
    needToRemove = []
    for a in newsDictionary["articles"]:
        if (a["title"] is None) or (a["title"] == "") or (a["urlToImage"] is None) or (a["urlToImage"] == ""):
            needToRemove.append(a)

    for a in needToRemove:
        newsDictionary["articles"].remove(a)
    newsDictionary["totalResults"] = len(newsDictionary["articles"])


def removeUnwantedSources(newsDictionary, unwantedSourcesId):
    if unwantedSourcesId:
        for a in newsDictionary["articles"]:
            for unwanted in unwantedSourcesId:
                if a["source"]["id"] is None or unwanted in a["source"]["id"]:
                    a["title"] = None


def isInException(exceptions, sid):
    b = False
    for e in exceptions:
        if (sid is not None and e in sid.lower()):
            b = True
    return b


def isInString(substring, s):
    return s is not None and substring in s.lower()


def removeOccurences(wordsToRemove, newsDictionary, blockingPourcentage, exception):
    for a in newsDictionary["articles"]:
        for m in wordsToRemove:
            if not (isInException(exception, a["source"]["id"])):
                if isInString(m, a["title"]) or isInString(m, a["description"]) or isInString(m, a["url"]) or isInString(m, a["urlToImage"]) or isInString(m, a["content"]):
                    i = randrange(100)
                    if i <= blockingPourcentage:
                        a["title"] = None


def saveSource(dic):
    source = []
    for a in dic["articles"]:
        if a["source"]["id"] is not None and a["source"]["name"] is not None and a["source"] is not None and a["source"] not in source:
            source.append(a["source"])
    return source


def getNewsHeadlines(news_api, page_size, category, country):
    return news_api.get_top_headlines(category=category, page_size=page_size, country=country)


def writeInFile(file, dataJson):
    with open(file, 'w') as f:
        json.dump(dataJson, f)


def cleanData(wordsToRemove, data, blockingPourcentage, exception, unwantedSource):
    removeOccurences(wordsToRemove, data,
                     blockingPourcentage, exception)
    removeUnwantedSources(data, unwantedSource)

    removeEmptyEntries(data)

    data.update(sources=saveSource(data))
    data.update(painting=getPaintingURL())


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
        objectId = response['objectIDs'][randrange(
            0, int(response['total']))]
        reply = requests.get(
            "https://collectionapi.metmuseum.org/public/collection/v1/objects/{}".format(str(objectId))).json()
        name = reply['title']
        artist = reply['artistDisplayName']
        url = reply['primaryImage']
        dick = {
            'name': name,
            'artist': artist,
            'url': url
        }
        return dick
        


def sendRequests(blockingPourcentage, category, country, exception):
    if category not in GOOGLE_CATEGORY and category is not None:
        return ERR_DIC
    news_api = NewsApiClient(api_key=API_KEY)

    top_headlines_no_filter = getNewsHeadlines(
        news_api, MAX_PAGE_SIZE, category, country)

    cleanData(MOTS_CORONA, top_headlines_no_filter,
              blockingPourcentage, exception, UNWANTED_SOURCES_ID)
    top_headlines_no_filter.update({"categories": GOOGLE_CATEGORY})
    return top_headlines_no_filter


def changeFormat(dic):
    newDic = {}
    newDic.update({"status": "ok", "totalResults": len(
        dic["results"]), "articles": []})
    for a in dic["results"]:
        art = {}
        source = {"id": "nyt", "name": "Ney York Times"}
        art.update({"source": source, "author": a["byline"], "title": a["title"], "description": a["abstract"],
                    "url": a["url"], "urlToImage": a["multimedia"][0]["url"], "publishedAt": a["published_date"], "content": ""})
        newDic["articles"].append(art)
    return newDic


def getNYTData(blockingPourcentage, category):
    if category not in NYT_CATEGORY and category is not None:
        return ERR_DIC
    if category is None:
        category = "home"
    url = "https://api.nytimes.com/svc/topstories/v2/" + category + ".json"
    data = requests.get(
        url, params={"api-key": NYT_KEY}).json()
    data = changeFormat(data)
    cleanData(MOTS_CORONA, data, blockingPourcentage, [], [])
    data.update({"categories": NYT_CATEGORY})
    return data


def splitException(exception):
    if exception is not None:
        return exception.split('_,')
    else:
        return []


@app.route('/news', methods=['GET', 'POST'])
def makeRequest():
    if request.method == "POST":
        api = request.form.get('api')
        blockingPourcentage = int(request.form.get('blockingPourcentage'))
        category = request.form.get('category')
        country = request.form.get('country')
        exception = request.form.get('exception')
        exception = splitException(exception)
    else:
        api = request.args.get('api')
        blockingPourcentage = int(request.args.get('blockingPourcentage'))
        category = request.args.get('category')
        country = request.args.get('country')
        exception = request.args.get('exception')
        exception = splitException(exception)

    if api == "nyt":
        return getNYTData(blockingPourcentage, category)
    elif api == "google":
        return jsonify(sendRequests(blockingPourcentage, category, country, exception))
    else:
        return ERR_DIC


## MAIN ##
app.run('localhost', port=1415)
