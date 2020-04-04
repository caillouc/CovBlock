import json
from newsapi import NewsApiClient
from random import randrange
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


def removeOccurences(wordsToRemove, newsDictionary, blokingPourcentage):
    needToRemove = []
    for a in newsDictionary["articles"]:
        for m in wordsToRemove["en"]:
            if ((a["title"] is not None and m in a["title"].lower()) or (a["description"] is not None and m in a["description"].lower()) or (a["url"] is not None and m in a["url"].lower()) or (a["urlToImage"] is not None and m in a["urlToImage"].lower()) or (a.get("content") is not None and m in a["content"].lower())):
                if a not in needToRemove:
                    needToRemove.append(a)

    for a in needToRemove:
        i = randrange(100)
        if i <= blokingPourcentage:
            newsDictionary["articles"].remove(a)
    newsDictionary["totalResults"] = len(newsDictionary["articles"])


def getNewsHeadlines(news_api, language, page_size):
    return news_api.get_top_headlines(language=language, page_size=page_size)


def writeInFile(file, dataJson):
    with open(file, 'w') as f:
        json.dump(dataJson, f)


def main():

    blokingPourcentage = 50
    news_api = NewsApiClient(api_key=API_KEY)
    top_headlines_no_filter = getNewsHeadlines(
        news_api, 'en', MAX_PAGE_SIZE)
    writeInFile("INITIAL_DATA.json", top_headlines_no_filter)
    removeOccurences(MOTS_CORONA, top_headlines_no_filter, blokingPourcentage)
    writeInFile('FILTERED_DATA.json', top_headlines_no_filter)


if __name__ == '__main__':
    main()
