# Twittercount

This program was originally built to get the tweet counts for ethereum specifically, using the official Twitter api. This program will get the number of tweets for a specific keyword that were generated from a designated time in the past up to the present time. 

## Instructions

* Fill out the keys in hidden.py 
* Run twittercount.py 
* Enter the keyword
* Limitations are noted in the Limitations section


### Limitations 
* This program can bring forth accurate counts only when there are less than 100 tweets generated in the 2 minute timeframe for the input keyword

* The number of requests is limited to 180 which means it can only count up to 6 hours worth of data when set to 2 min timeframe


### Libraries 
* urllib
* ssl 
* json 
* datetime 



## Built With

* [Pycharm](https://www.jetbrains.com/pycharm/) 




## Authors

* **Jae Hyun Moon** 



## Acknowledgments

* hidden.py, oauth.py, twurl.py by [Charles R. Severance] (https://www.py4e.com/code3)

