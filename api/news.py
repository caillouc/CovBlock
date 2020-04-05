from newsapi import NewsApiClient
from random import randrange
from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import time
import sys

app = Flask(__name__)
CORS(app)

## CONSTANTES ##
API_KEY = "f0a443efaaec4868978a2e693c779496"
MOTS_CORONA = ["corona", "covid", "covid-19", "coronavirus",
               "confinement", "quarantaine", "quinzaine", "wuhan", "lockdown", "quarantine", "face mask"]

UNWANTED_SOURCES_ID = ["hacker-news"]

MAX_PAGE_SIZE = 100


## METHODES ##

def removeEmptyEntries(newsDictionary):
    needToRemove = []
    for a in newsDictionary["articles"]:
        if a["title"] is None or a["title"] == '' or a["urlToImage"] is None or a["urlToImage"] == '':
            if a not in needToRemove:
                needToRemove.append(a)

    for a in needToRemove:
        newsDictionary["articles"].remove(a)
    newsDictionary["totalResults"] = len(newsDictionary["articles"])


def removeUnwantedSources(newsDictionary, unwantedSourcesId):
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
        if a["source"] is not None and a["source"] not in source:
            source.append(a["source"])
    return source


def getNewsHeadlines(news_api, page_size, category, country):
    return news_api.get_top_headlines(category=category, page_size=page_size, country=country)


def writeInFile(file, dataJson):
    with open(file, 'w') as f:
        json.dump(dataJson, f)


def sendRequests(blockingPourcentage, category, country, exception):
    news_api = NewsApiClient(api_key=API_KEY)

    top_headlines_no_filter = getNewsHeadlines(
        news_api, MAX_PAGE_SIZE, category, country)

    #top_headlines_no_filter = {}
    # with open("init.json", "r") as f:
    #    top_headlines_no_filter = json.load(f)

    removeOccurences(MOTS_CORONA, top_headlines_no_filter,
                     blockingPourcentage, exception)
    removeUnwantedSources(top_headlines_no_filter, UNWANTED_SOURCES_ID)

    removeEmptyEntries(top_headlines_no_filter)

    sources = saveSource(top_headlines_no_filter)
    top_headlines_no_filter.update(sources=sources)

    writeInFile("data.json", top_headlines_no_filter)
    return top_headlines_no_filter


def splitException(exception):
    if exception is not None:
        return exception.split()
    else:
        return []


@app.route('/news', methods=['GET', 'POST'])
def makeRequest():
    # list category : business entertainment general health science sports technology
    if request.method == "POST":
        blockingPourcentage = int(request.form.get('blockingPourcentage'))
        category = request.form.get('category')
        country = request.form.get('country')
        exception = request.form.get('exception')
        exception = splitException(exception)
    else:
        blockingPourcentage = int(request.args.get('blockingPourcentage'))
        category = request.args.get('category')
        country = request.args.get('country')
        exception = request.args.get('exception')
        exception = splitException(exception)
    return jsonify(sendRequests(blockingPourcentage, category, country, exception))


## MAIN ##
app.run('localhost', port=1415)
