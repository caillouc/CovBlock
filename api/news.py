from newsapi import NewsApiClient
from random import randrange
from flask import Flask, request, jsonify
import json
import time
import sys

app = Flask(__name__)

## CONSTANTES ##
API_KEY = "f0a443efaaec4868978a2e693c779496"
MOTS_CORONA = {
    "fr": ["corona", "covid", "covid-19", "coronavirus",
           "confinement", "quarantaine", "quinzaine", "wuhan"],
    "en": ["corona", "covid", "covid-19", "coronavirus",
           "lockdown", "quarantine", "wuhan"]
}
MAX_PAGE_SIZE = 100


## METHODES ##

def removeEmptyEntries(newsDictionary):
    needToRemove = []
    for a in newsDictionary["articles"]:
        if(a["title"] is None or a["title"] == ''):
            needToRemove.append(a)

    for a in needToRemove:
        newsDictionary["articles"].remove(a)
    newsDictionary["totalResults"] = len(newsDictionary["articles"])


def removeOccurences(wordsToRemove, language, newsDictionary, blockingPourcentage):
    needToRemove = []
    if language is None:
        language = 'en'
    for a in newsDictionary["articles"]:
        for m in wordsToRemove[language]:
            if ((a["title"] is not None and m in a["title"].lower()) or (a["description"] is not None and m in a["description"].lower()) or (a["url"] is not None and m in a["url"].lower()) or (a["urlToImage"] is not None and m in a["urlToImage"].lower()) or (a.get("content") is not None and m in a["content"].lower())):
                if a not in needToRemove:
                    needToRemove.append(a)
    for a in needToRemove:
        i = randrange(100)
        if i <= blockingPourcentage:
            newsDictionary["articles"].remove(a)
    newsDictionary["totalResults"] = len(newsDictionary["articles"])


def getNewsHeadlines(news_api, language, page_size, category, country):
    if language is None:
        language = 'en'
    return news_api.get_top_headlines(category=category, language=language, page_size=page_size, country=country)


def writeInFile(file, dataJson):
    with open(file, 'w') as f:
        json.dump(dataJson, f)


def sendRequests(blockingPourcentage, language, category, country):

    news_api = NewsApiClient(api_key=API_KEY)
    top_headlines_no_filter = getNewsHeadlines(
        news_api, language, MAX_PAGE_SIZE, category, country)
    writeInFile("INITIAL_DATA.json", top_headlines_no_filter)
    removeEmptyEntries(top_headlines_no_filter)
    removeOccurences(MOTS_CORONA, language,
                     top_headlines_no_filter, blockingPourcentage)
    writeInFile('FILTERED_DATA.json', top_headlines_no_filter)
    return top_headlines_no_filter


@app.route('/news', methods=['POST'])
def makeRequest():
    # business entertainment general health science sports technology
    # for get : args.get
    # fro post .form
    blockingPourcentage = int(request.form.get('blockingPourcentage'))
    language = request.form.get('language')
    category = request.form.get('category')
    country = request.form.get('country')
    #print("blokingPourcentage : " + str(blockingPourcentage))
    #print("language : " + language)
    #print("category : " + category)
    #print("country : " + country)
    return jsonify(sendRequests(blockingPourcentage, language, category, country))


## MAIN ##
app.run('localhost', port=1415)
