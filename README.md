# @DailyWineBot Twitter Bot

Twitter bot scheduled to pull random wine info from Snooth.com and tweet once per day.

## Tech
* Python 3.6+ - makes use of f-strings (introduced in 3.6)
* Tweepy - Python library to ineract with the Twitter API
* Requests - Python library to make HTTP requests
* Heroku - Deployed and uses the Heroku Scheduler 

## Launch
Must have Twitter and Snooth account credentials.

This is deployed on Heroku and uses their Scheduler. In Heroku settings, Buildpack should be heroku/python, and Config Vars for Twitter and Snooth must be set. 

requirements.txt file incldues the tweepy and requests library dependecies to be included. 

Procfile includes the worker command run daily via Scheduler.

The worker command executes dailywinebot.py which calls getdata.py

## Thanks
This app tweets data provided from Snooth, an online community for wine lovers. Links for info:
[Snooth.com](http://www.snooth.com/)
[Snooth_API](https://api.snooth.com/)

