# 326final
# About

The purpose of this tool is to search through tweets using a real-time Twitter API to visualize the sentiments of 2020 U.S. presidential candidates. Users can search for up to 18 candidates that are currently in the race, as December 12th, 2019. The scope of this project is limited by analyzing 200 tweets per candidate, for each query. This program will graph the percentage of positive, negative and neutral sentiments towards each candidate in the form of three separate pie charts. 

Keep up in mind that [Twitter statuses/filter API](https://developer.twitter.com/en/docs/tweets/filter-realtime/overview.htmls) has a 400 keywords limit for streaming realtime tweets.

# Requirements

To run this script, you'll need python 3.7 and the following libraries: 

* [Tweepy](https://github.com/tweepy/tweepy)
* [TextBlob](https://textblob.readthedocs.io/en/dev/)
* Datetime
* MatPlotLib and PyPlot
* Sys 

# Running the application

This is a command line program. When running this script in your terminal, please type in the Twitter handle of each 2020 Presidential candidate that you are interested in learning about OR type ‘all’ to view the results of all 18 candidates who are still in the race. 

Example command line: 
‘Python3 filename.py @TulsiGabbard @realDonalTrump @ewarren’

Please note that currently when the program runs all three graph windows will likely pop-up directly behind one another. Please drag the windows to view all three next to each other.


