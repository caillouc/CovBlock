# How to use news API 

## how to communicate with our api

* In order to request data, you will have to use the `POST` method in `/news`. In order to send you back all the articles, we need a value between 0 and 100 in a field named `blockingPourcentage`. This value can be given as a String and then we will cast it into an int (we are not using a try, excpet so please make sure that the given string can correctly be cast in an int). We assume that `blockingPourcentage` is bigger or equal to 0 and less or equal than 100. 
  
* First option: You can also provide us a category in the field `category`. This category can either be `business`,  `entertainment`,  `general`, `health`,  `science`,  `sports` or `technology`.

* Second option: You can also complete the field `country` with one of those value : `ae ar at au be bg br ca ch cn co cu cz de eg fr gb gr hk hu id ie il in it jp kr lt lv ma mx my ng nl no nz ph pl pt ro rs ru sa se sg si sk th tr tw ua us ve za`. 

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

--- 
[Bisous](https://cartes-virtuelles.joliecarte.com/petites-attentions/carte-bisous.jpg)



