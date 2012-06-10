# Import required libraries
import twitter
import ConfigParser

# Import settings from config file
config = ConfigParser.RawConfigParser()
config.read('twitter.cfg')

# Make connection to twitter API
consumer_key = config.get('API', 'consumer_key')
consumer_secret = config.get('API', 'consumer_secret')
access_token_key = config.get('API', 'access_token_key')
access_token_secret = config.get('API', 'access_token_secret')

api = twitter.Api( consumer_key, consumer_secret, access_token_key, access_token_secret)

# Verify API credentials by requesting public timeline
statuses = api.GetPublicTimeline()
print [s.user.name for s in statuses]
 
