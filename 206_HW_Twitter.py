import unittest
import tweepy
import requests
import json
import twitter_info

## SI 206 - HW
## COMMENT WITH:
## Your section day/time: Lecture 001 2:30-4 MoWed, Discussion 005 6-7 Thur
## Any names of people you worked with on this assignment: N/A


## Write code that uses the tweepy library to search for tweets with three different phrases of the 
## user's choice (should use the Python input function), and prints out the Tweet text and the 
## created_at value (note that this will be in GMT time) of the first FIVE tweets with at least 
## 1 blank line in between each of them, e.g.


## You should cache all of the data from this exercise in a file, and submit the cache file 
## along with your assignment. 

## So, for example, if you submit your assignment files, and you have already searched for tweets 
## about "rock climbing", when we run your code, the code should use CACHED data, and should not 
## need to make any new request to the Twitter API.  But if, for instance, you have never 
## searched for "bicycles" before you submitted your final files, then if we enter "bicycles" 
## when we run your code, it _should_ make a request to the Twitter API.

## Because it is dependent on user input, there are no unit tests for this -- we will 
## run your assignments in a batch to grade them!

## We've provided some starter code below, like what is in the class tweepy examples.

##SAMPLE OUTPUT
## See: https://docs.google.com/a/umich.edu/document/d/1o8CWsdO2aRT7iUz9okiCHCVgU5x_FyZkabu2l9qwkf8/edit?usp=sharing



## **** For extra credit, create another file called twitter_info.py that 
## contains your consumer_key, consumer_secret, access_token, and access_token_secret, 
## import that file here.  Do NOT add and commit that file to a public GitHub repository.

## **** If you choose not to do that, we strongly advise using authentication information 
## for an 'extra' Twitter account you make just for this class, and not your personal 
## account, because it's not ideal to share your authentication information for a real 
## account that you use frequently.

## Get your secret values to authenticate to Twitter. You may replace each of these 
## with variables rather than filling in the empty strings if you choose to do the secure way 
## for EC points
consumer_key = twitter_info.consumer_key 
consumer_secret = twitter_info.consumer_secret
access_token = twitter_info.access_token
access_token_secret = twitter_info.access_token_secret
## Set up your authentication to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
# Set up library to grab stuff from twitter with your authentication, and 
# return it in a JSON-formatted way

api = tweepy.API(auth, parser=tweepy.parsers.JSONParser()) 

## Write the rest of your code here!

#### Recommended order of tasks: ####
## 1. Set up the caching pattern start -- the dictionary and the try/except 
## 		statement shown in class.
CACHE_FNAME = 'tweet_contents.json'
try:
	cache_file = open(CACHE_FNAME, 'r') # Opens the file that contains cached information
	cache_contents = cache_file.read()  # Turns data into python readable content
	CACHE_DICTION = json.loads(cache_contents) # reads in that file and puts it into a json formatted dictionary
	cache_file.close() # closes the file
except:
	CACHE_DICTION = {} # If there is nothing in the file, set cache to an empty dictionary



## 2. Write a function to get twitter data that works with the caching pattern, 
## 		so it either gets new data or caches data, depending upon what the input 
##		to search for is.
def get_data_with_caching(tweet_term):
	if tweet_term in CACHE_DICTION:
		print('using cache')
		return CACHE_DICTION[tweet_term] # if the term has already been searched and is in the cache dictionary, use that 
	else:
		print('fetching')
		results = api.search(q=tweet_term) #if it has not been searched use tweepy to search that term
		CACHE_DICTION[tweet_term] = results # adds the tweet term as a key and the results from tweepy as the value
		dumped_json_cache = json.dumps(CACHE_DICTION) # creates an object of the updated cache dictionary
		cache_file = open(CACHE_FNAME, 'w')
		cache_file.write(dumped_json_cache) # writes the new dictionary in the cache file
		cache_file.close()
		return CACHE_DICTION[tweet_term] # returns the search of the term that is now in the cache dictionary



## 3. Using a loop, invoke your function, save the return value in a variable, and explore the 
##		data you got back!
for num in range(3): # range three so the user will be prompted 3 times then the program will end
	user_input = input('Enter Tweet term: ') # prompts user with what they want to search
	tweet_term = str(user_input)
	tweet_data = get_data_with_caching(tweet_term) # calls get_with_caching to either store tweet term data in cache and get data, or just get data from cache 
## 4. With what you learn from the data -- e.g. how exactly to find the 
##		text of each tweet in the big nested structure -- write code to print out 
## 		content from 5 tweets, as shown in the linked example.
	for tweet in tweet_data['statuses'][:5]: # takes the top 5 tweets in the data 
		print('TEXT: {}'.format(tweet['text'])) # states the text of the tweet
		print('CREATED AT: {}'.format(tweet['created_at'])) # states when the tweet was posted
		print('\n')









