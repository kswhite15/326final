import tweepy
from textblob import TextBlob
from matplotlib import pyplot as plt
import datetime
import sys



auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

class CandidateAnalysis():
    '''DOCSTRING FOR CLASS'''
    def __init__(self, single_candidate):
        '''DOCSTRING FOR METHOD'''
        self.candidate = single_candidate

    def sentiment(self, single_candidate):
        '''DOCSTRING FOR METHOD'''
        # This is a variable which searches Twitter using its
        # API to retrive up to 200 tweets relating to the candidate handle
        # that was searched:
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


def pie_chart(sys_list):

    positive = [] #count of pos tweets for each candiate [150, 200, 400]
    negative= [] #count of neg tweets for each candiate [150, 200, 400]
    neutral= [] #count of neu tweets for each candiate [150, 200, 400]

    for candidate_name in sys_list:
        conduct_analysis = CandidateAnalysis(candidate_name)
        instance_sentiment = conduct_analysis.sentiment(candidate_name)

        pos_count=0
        neu_count=0
        neg_count=0
        for single_sentiment in conduct_analysis.candidate_sentiment:
            if single_sentiment == 0:
                neu_count+=1
            elif single_sentiment < 0:
                neg_count +=1
            else:
                pos_count +=1
        positive.append(pos_count)
        negative.append(neg_count)
        neutral.append(neu_count)


    #Here is a unit test:
    try:
        print('Unit testing in progress...')
        assert len(positive) == 1 #THIS TEST FAILS ON the second to last candiate searched AND IM NOT SURE WHY?
        assert len(neutral) == 1
        assert len(negative) == 1
    except:
        print("Pos, Neu, Neg count test failed!")


    rainbow = ['red','orange','yellow','green','blue','purple','violet',
            'pink', 'teal','yellowgreen', 'gold', 'coral', 'lavenderblush',
            'skyblue','lime', 'indigo','cyan','magenta']

    #"explode" the candidate that the user enters, use autopct='%1.1f%%'

    length_list = len(sys_list)
    color_list = []
    for item in rainbow[0:length_list]:
        color_list.append(item)


    #Here is a unit test:
    try:
        print('Unit testing in progress...')
        assert len(color_list) == len(sys_list)
    except:
        print("Color list test failed!")


    plt.figure(1)
    plt.pie(positive,labels= sys_list, autopct= '%1.1f%%', colors=color_list)
    plt.title("Postive Tweets", size=24, weight='bold')
    plt.axis('equal')

    plt.figure(2)
    plt.pie(negative, labels= sys_list, autopct= '%1.1f%%', colors=color_list)
    plt.title("Negative Tweets", size=24, weight='bold')
    plt.axis('equal')

    plt.figure(3)
    plt.pie(neutral, labels= sys_list, autopct= '%1.1f%%', colors=color_list)
    plt.title("Neutral Tweets",size=24, weight='bold')
    plt.axis('equal')
    plt.rcParams['font.size'] = 12
    plt.show()

def all_candidates(sys_list):
    if sys_list[0] == "all":
        sys_list= ["@MichaelBennet", "@JoeBiden", "@MikeBloomberg","@CoryBooker",
        "@PeteButtigieg", '@JulianCastro', "@JohnDelaney", "@TulsiGabbard",
        "@amyklobuchar", "@DevalPatrick","@BernieSanders","@TomSteyer",
        "@ewarren","@marwilliamson","@AndrewYang","@realDonaldTrump", "@WalshFreedom","@GovBillWeld"]
        pie_chart(sys_list)

# If the user has not entered in at least two handles for comparison
# into the initial sys.argv in the command line, then run this script:
if len(sys.argv) < 3:
    sys_list = []
    while True:
        print("Enter ALL the candidate handles you would like to search")
        search_string = input('Use the format "@Candidate" (q to quit): ')
        split_search_string = search_string.split()
        for candidate_name in split_search_string:
            if candidate_name == "q":
                continue
            else:
                sys_list.append(candidate_name)


        # This is a unit test:
        try:
            print('Unit testing in progress...')
            assert "q" not in sys_list
        except:
            print("'Q' in sys_list test failed!")


        all_candidates(sys_list)
        if search_string == "q":

            # Checks to make sure that it should not run the pie_chart
            # function if the all_candidates function has already been run:
            if "all" not in sys_list:
                pie_chart(sys_list)
                break

# If the user has entered two handles for comparison, or more,
# into the initial sys.argv in the command line then run this script:
elif len(sys.argv) >= 3:
    sys_list = sys.argv[1:]
    all_candidates(sys_list)

    # Checks to make sure that it should not run the pie_chart
    # function if the all_candidates function has already been run:
    if "all" not in sys_list:
        pie_chart(sys_list)
