# 326final
# About

Python script for connecting to Twitter stream, gather tweets that match a particular keyword, hashtag or mention and save them on a CSV file.

Keep up in mind that [Twitter statuses/filter API](https://developer.twitter.com/en/docs/tweets/filter-realtime/overview.htmls) has a 400 keywords limit for streaming realtime tweets.

`sample-tweets.csv` is a sample file for a search around SEO.

# Requirements

To run this script, you'll need python 3.7 and the following libraries: 

* [Tweepy](https://github.com/tweepy/tweepy)
* [TextBlob](https://textblob.readthedocs.io/en/dev/)
* Sys.argv
* Datetime
* MatPlotLib and PyPlot

# Running the application

Clone this repository to your computer. Finally, within the cloned folder, type the following in the command line to run the script locally:

`python3 stream.py`
