#!/usr/bin/env python3
'''
Name: Isabeau Rea, Richa Dhamankar, Chinemerem Iweala,
        Ani Tansinda, Kennedy Whitehead
Directory ID: 115105591, 115887923, 115945265, 116038874, 114713650
Date: 2019-12-12
Assignment: Final Project
'''

import tweepy

from textblob import TextBlob

from matplotlib import pyplot as plt

import datetime

import sys


# Define consumer keys and access tokens
consumer_key = '' #your key here
consumer_secret = '' #your key here
access_token = '' #your key here
access_token_secret = '' #your key here


# Access Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


class CandidateAnalysis():
    '''A class which creates a unique instance for every
    candidate the user searches. It then gets the search results
    for this candidate name, and conducts the sentiment analysis
    on tweets about this candidate. This class also contains two
    unit tests.'''


    def __init__(self, single_candidate):
        '''Create attribute for a single candidate'''
        
        self.candidate = single_candidate


    def sentiment(self, single_candidate):
        '''This is a variable which searches Twitter using its
        API to retrive up to 200 tweets relating to the
        candidate handle that was searched:'''
        
        public_tweets=api.search(single_candidate, count = 200)


        #Here is a unit test:
        try:
            print('Unit testing in progress...')
            assert len(public_tweets) > 0
        except:
            print("Public tweets test failed!")


        self.candidate_sentiment = []

        for tweet in public_tweets:
            
            analysis= TextBlob(tweet.text)
            
            self.candidate_sentiment.append(analysis.sentiment[0])


        #Here is a unit test:
        try:
            print('Unit testing in progress...')
            assert len(self.candidate_sentiment) > 0
        except:
            print("Candidate Sentiment list test failed!")

def main(CandidateAnalysis):
    '''The main function for our script. Takes CandidateAnalysis class as
    a parameter. The function calculates and displays the pie chart for the
    canidates that the user searches. It allows for the user to search
    in the initial sys.argv terminal entry, or incrementally, through
    user input. It also allows the user to enter in "all" to search every
    candidate without having to enter them in one by one.'''


    def pie_chart(sys_list):
        '''Create Graphs of Tweet Sentiment separated by feeling'''
        
        #count of pos tweets for each candiate [150, 200, 400]
        positive = []
        
        #count of neg tweets for each candiate [150, 200, 400]
        negative= []
        
        #count of neu tweets for each candiate [150, 200, 400]
        neutral= []

        
        for candidate_name in sys_list:

            conduct_analysis = CandidateAnalysis(candidate_name)

            instance_sentiment = conduct_analysis.sentiment(candidate_name)

                
            #initalizes sentiment counts
            pos_count=0
            neu_count=0
            neg_count=0

                
            #grading individual tweet sentiments
            for single_sentiment in conduct_analysis.candidate_sentiment:

                if single_sentiment == 0:
                    neu_count+=1

                elif single_sentiment < 0:
                    neg_count +=1

                else:
                    pos_count +=1

                
            #appending candidate's total counts to the repsective lists
            positive.append(pos_count)
            negative.append(neg_count)
            neutral.append(neu_count)


        # This is the color scheme for pie chart
        RAINBOW = ['red','orange','yellow','green','blue','purple','violet',
                'pink', 'teal','yellowgreen', 'gold', 'coral', 'lavenderblush',
                'skyblue','lime', 'indigo','cyan','magenta']

        
        length_list = len(sys_list)

        color_list = []

        for item in RAINBOW[0:length_list]:
            color_list.append(item)


        #Here is a unit test:
        try:
            print('Unit testing in progress...')
            assert len(color_list) == len(sys_list)
        except:
            print("Color list test failed!")

        
        # postive tweets graph
        plt.figure(1) #creates seprate graphs

        plt.pie(positive,labels= sys_list,autopct='%1.1f%%',colors=color_list)

        # labeling pie sections by candidate, displaying the percetange
        # they have, and assigning clearly defined colors

        plt.title("Postive Tweets", size=24, weight='bold') #Bold title

        plt.axis('equal') #makes sure graph is a uniform circle


        #negative tweets graph
        plt.figure(2)

        plt.pie(negative, labels= sys_list, autopct= '%1.1f%%', colors=color_list)

        plt.title("Negative Tweets", size=24, weight='bold')

        plt.axis('equal')


        #neutral tweets graph
        plt.figure(3)

        plt.pie(neutral, labels= sys_list, autopct= '%1.1f%%', colors=color_list)

        plt.title("Neutral Tweets",size=24, weight='bold')

        plt.axis('equal')

        plt.rcParams['font.size'] = 12

        plt.show()

        
    def all_candidates(sys_list):
        '''Create pie chart for all candidates currently in the race'''

        
        if sys_list[0] == "all":

            sys_list= ["@MichaelBennet", "@JoeBiden", "@MikeBloomberg",
            "@CoryBooker", "@PeteButtigieg", '@JulianCastro',
            "@JohnDelaney", "@TulsiGabbard", "@amyklobuchar",
            "@DevalPatrick","@BernieSanders","@TomSteyer", "@ewarren",
            "@marwilliamson","@AndrewYang","@realDonaldTrump",
            "@WalshFreedom","@GovBillWeld"]

            pie_chart(sys_list)

                
    # Empty list to hold command line arguments
    sys_list = []

        
    # If the user has not entered in at least two handles for comparison
    # into the initial sys.argv in the command line, then run this script:
    if len(sys.argv) < 3:

        
        while True:

            print("Enter ALL the candidate handles you would like to search")
            print('Use the format "@Candidate"')
            print('To conduct a fresh search with all new search terms, re-run the program.')
        
           
            search_string = input('(Enter graph to make graph, q to quit): ')


            # This checks to see if the user is trying to quit. If so it
            # adds 1 to a counter which is checked to see if it equals 1.
            # If it equals 1, then the script quits.
            q_entered = 0

            if search_string == "q":
                q_entered += 1

            if q_entered == 1:
                break


            split_search_string = search_string.split()
            
            for candidate_name in split_search_string:

                if candidate_name == "q":
                    break

                elif candidate_name == "graph":
                    continue

                elif len(sys_list) >= 18:
                    print("Sorry, you cannot have more than 18 search terms.")
                    print("Please enter 'q' to generate your graph now")

                else:
                    sys_list.append(candidate_name)


        # This is a unit test:
            try:
                print('Unit testing in progress...')
                assert "q" not in sys_list
            except:
                print("'Q' in sys_list test failed!")


            all_candidates(sys_list)


            if search_string == "graph":
            
            # Checks to make sure that it should not run the pie_chart
            # function if the all_candidates function has already been run:
                if "all" not in sys_list:
                    pie_chart(sys_list)


    # If the user has entered two handles for comparison, or more,
    # into the initial sys.argv in the command line then run this script:
    elif len(sys.argv) >= 3:

        sys_list = sys.argv[1:]

        all_candidates(sys_list)

        
        # Checks to make sure that it should not run the pie_chart
        # function if the all_candidates function has already been run:
        if "all" not in sys_list:
            pie_chart(sys_list)


if __name__ == "__main__":
    main(CandidateAnalysis)
