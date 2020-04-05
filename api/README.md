# How to use news API 

## How to communicate with our api

* In order to request data, you will have to use the `POST` method in `/news`. In order to send you back all the articles, we need a value between 0 and 100 in a field named `blockingPourcentage`. This value can be given as a String and then we will cast it into an int (we are not using a try, excpet so please make sure that the given string can correctly be cast in an int). We assume that `blockingPourcentage` is bigger or equal to 0 and less or equal than 100. We also need the value `nyt`or `google` in the `api` field. This field allows you to select from wich api you want to retrieve data.
  
* First option: You can also provide us a category in the field `category`. This categories depends on the api you choose. You received the correct list in the field `categories` 

* Second option (only for google api): You can also complete the field `country` with one of those value : `ae ar at au be bg br ca ch cn co cu cz de eg fr gb gr hk hu id ie il in it jp kr lt lv ma mx my ng nl no nz ph pl pt ro rs ru sa se sg si sk th tr tw ua us ve za`. 

* Third option (only for google api): A String with all the excpetions ids separate with a space. For example `cnn bbc-news`. You can find all the possible source in the field `sources`.

## How to use our server in localhost 

* First you need to install some stuff. Run those two cammands :

```bash
$ pip3 install flask
$ pip3 install newsapi-python
$ pip3 install flask-cors
```

* Then go in `api/` folder and run the following command :

```zsh
$ python3 news.py
````

* To send an http post request to can use `httpie`. You can install it with : 

```zsh
$ sudo apt install httpie
```

You might need to use `pacman` or `brew` instead of `apt` depending on your operating sytem

Then you can use this command : 

```zsh 
$ http -f POST localhost:1415/news blockingPourcentage="100" 
```

or : 

```zsh
$ http -f POST localhost:1415/news blockingPourcentage="100" category="sports" country="fr"
````

or use the get method :
```zsh
$ http http://localhost:1415/news\?blockingPourcentage\=100\&country\=fr
```

## Bonus 

* You can find a beautifull painting in the field `painting`

--- 
[Bisous](https://cartes-virtuelles.joliecarte.com/petites-attentions/carte-bisous.jpg)



