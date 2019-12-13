# 326final
# About

Live-tweeting is the act of a Twitter user posting tweets in real time of their responses to an event, and in this case, the 2020 presidential debates. The advent of the phenomenon of "live-tweeting" presidential debates on Twitter brings with it a desire for a more immersive way to participate and understand that practice. 

To fulfill this desire is Petty Politician (the name serving as a tongue-in-cheek nod to the increasingly dramatic culture of the debates and those who tweet about them). Users enjoy not only voicing their own opinions on what a given candidate has just said, but also gauging if their sentiment is shared by others. This is what Petty Politician seeks to provide– a tool to understand how Twitter users feel about the statements a candidate has made during a given debate in real-time to make the user feel more connected with others in their feelings.

To accomplish this aim, the program searches through tweets using a real-time Twitter API to visualize the sentiments of the 2020 U.S. presidential candidates the user queries. Visualizations of the sentiments about the candidates the user searched are displayed in a series of three pie charts for the percentage of total tweets that were positive, negative, and neutral in their sentiments. 

# Features of the Search
* Users can search for up to 18 candidates that are currently in the race, as of December 12th, 2019. 
* There is also an option for the user to enter "all" as a search, which will save them time through concisely searching for each candidate and returning results without the user having to enter in each candidate as a search.
* Users can enter in a search of two or more candidates for comparison in their initial sys.argv command line entry to run the script.
* Users can also run the script without an initial search. 
* NOTE: If they choose to do a search in the initial command line, they will only be able to search once. If the user wants a more ongoing experience where they can generate several graphs or gradually search for candidates across several search entries, this is also possible. By running the script without an initial search term, the user will enter this interactive mode. 

# Constraints of the API
The scope of this project is limited by the constraints of the only Twitter API we were able to access for free which allows the retrieval of only up to 200 tweets for a given search, and only real-time searching with no feature for retrieving tweets outside of this time constraint. This created an exciting challenge to restructure our initial idea while remaining true to our users' needs and our core objective.

# Module Requirements

To run this script, you'll need python 3.7 and the following libraries: 

* [Tweepy](https://github.com/tweepy/tweepy)
* [TextBlob](https://textblob.readthedocs.io/en/dev/)
* Datetime
* MatPlotLib and PyPlot
* Sys 

# Running the application

This is a command line program. When running this script in your terminal, please type in the Twitter handle of each 2020 Presidential candidate that you are interested in learning about OR enter ‘all’ to view the results of all 18 candidates who are still in the race. 

*Example command line: 
‘Python3 filename.py @TulsiGabbard @realDonalTrump @ewarren’

*Example search if not entering a search into initial command line that runs the file:
'@TulsiGabbard @realDonalTrump @ewarren'

*How to quit from the interactive search:
Enter 'q' into the search prompt

*How to generate a graph from the interactive search:
Enter 'graph' into the search prompt

Please note that currently when the program runs all three graph windows will likely pop-up directly behind one another. Please drag the windows to view all three next to each other.


