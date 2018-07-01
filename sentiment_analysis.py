import tweepy
from textblob import TextBlob
import re


# function to remove links and usernames from tweets
def clean(tweet):
    return re.sub(r'@\S+|https?://\S+', '', tweet)


# function that returns a sentiment description according to the threshold value
def get_sentiment(analysis, threshold):
    if analysis.sentiment.polarity > threshold:
        return 'positive'
    elif analysis.sentiment.polarity < -1.0*threshold:
        return 'negative'
    else:
        return 'neutral'


def main():
    # keys obtained from apps.twitter.com
    # replace the placeholder with appropriate values
    consumer_key = 'consumer key'
    consumer_secret = 'consumer secret'
    access_token = 'access token'
    access_token_secret = 'access token secret'
 
    try:
        # creates authentication handler object and set the access tokens
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        # creates api object to fetch tweets 
        api = tweepy.API(auth)
    
    except Exception as e:
        print('ERROR: Authentication failed')

    # collect public tweets on a specific topic
    query = input('\nEnter a topic to apply sentiment analysis on:\n\t')
    public_tweets = api.search(query, count = 10000)
    print()

    # list to hold dictionaries of parsed tweets
    tweets = []

    try:
        for tweet in public_tweets:
            parsed_tweet = {}
            
            # remove unwanted characters from tweet
            clean_tweet = clean(tweet.text)
            # create textblob object
            analysis = TextBlob(clean_tweet)

            # text of tweet
            parsed_tweet['text'] = clean_tweet
            # sentiment of tweet
            parsed_tweet['sentiment'] = get_sentiment(analysis, 0.1)
            # polarity of tweet
            parsed_tweet['polarity'] = analysis.sentiment.polarity
            # subjectivity of tweet
            parsed_tweet['subjectivity'] = analysis.sentiment.subjectivity

            # appending parsed tweet to tweets list
            if tweet.retweet_count > 0:
                # append once if tweet has retweets
                if parsed_tweet not in tweets:
                    tweets.append(parsed_tweet)
            else:
                tweets.append(parsed_tweet)
    
    except tweepy.TweepError as te:
        print('ERROR: ' + str(te))

    # filering tweets according to sentiment
    positive_tweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']    
    negative_tweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
    neutral_tweets = [tweet for tweet in tweets if tweet['sentiment'] == 'neutral']

    # print result percentage summary
    print('\nSentiment analysis results:')
    print('\tPositive\t{0:.2f} %'.format((len(positive_tweets)/len(tweets))*100))
    print('\tNegative\t{0:.2f} %'.format((len(negative_tweets)/len(tweets))*100))
    print('\tNeutral \t{0:.2f} %'.format((len(neutral_tweets)/len(tweets))*100))

    number = 5

    # print positive tweets
    print('\n\nPositive tweets:\n')
    for tweet in positive_tweets[:number]:
        print('\t> ' + tweet['text'])
        print('\tPolarity = {0:.3f} ; Subjectivity = {0:.3f}\n'.format(tweet['polarity'], tweet['subjectivity']))

    # print negative tweets
    print('\nNegative tweets:\n')
    for tweet in negative_tweets[:number]:
        print('\t> ' + tweet['text'])
        print('\tPolarity = {0:.3f} ; Subjectivity = {0:.3f}\n'.format(tweet['polarity'], tweet['subjectivity']))

    # print neutral tweets
    print('\nNeutral tweets:\n')
    for tweet in neutral_tweets[:number]:
        print('\t> ' + tweet['text'])
        print('\tPolarity = {0:.3f} ; Subjectivity = {0:.3f}\n'.format(tweet['polarity'], tweet['subjectivity']))


if __name__ == '__main__':
    main()