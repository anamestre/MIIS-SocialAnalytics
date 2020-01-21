import sys
import tweepy
import json


consumer_key = 'put yours here'
consumer_secret = 'put yours here'
access_token = 'put yours here'
access_token_secret = 'put yours here'

class StdOutListener(tweepy.StreamListener):

	def on_status(self, status):
		try:
			#tweet_json = json.loads(json.dumps(status._json))
			#print tweet_json
			print json.dumps(status._json)
		except:
			print "Unexpected error:", sys.exc_info()[0]
		return True
 
	def on_error(self, status_code):
		print('Got an error with status code: ' + str(status_code))
		return False # To continue listening
 
	def on_timeout(self):
		print('Timeout...')
		return False # To continue listening
 
if __name__ == '__main__':

	listener = StdOutListener()
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	stream = tweepy.Stream(auth, listener)
	#stream.filter(locations=[-6.38,49.87,1.77,55.81]) # coordinates of barcelona
	stream.filter(track=['your_search_term'])

