# Hox to use news API 

* In order to request data, you will have to use the `POST` method in `/news`. In order to send you back all the acticles, we need a value between 0 and 100 in a field named `blockingPoucentage`. This value can be given as a String and then we will cast it into an int (we are not using a try, excpet so please make sure that the given string can correctly be cast in an int). We assume that `blockingPourcentage` is bigger or equal to 0 and less or equal than 100. 
  
* First optioanl option: You can also provide us a category in the field `category`. This category can either be `business`,  `entertainment`,  `general`, `health`,  `science`,  `sports` or `technology`.

* Second optional option: You can also complete the field `country` with one of those value : `ae ar at au be bg br ca ch cn co cu cz de eg fr gb gr hk hu id ie il in it jp kr lt lv ma mx my ng nl no nz ph pl pt ro rs ru sa se sg si sk th tr tw ua us ve za`. 