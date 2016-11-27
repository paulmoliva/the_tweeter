import twitter

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
OAUTH_TOKEN = '-'
OAUTH_TOKEN_SECRET = ''
WORLD_WOE_ID = 1
US_WOE_ID = 23424977

api = twitter.Api(consumer_key=CONSUMER_KEY,
                      consumer_secret=CONSUMER_SECRET,
                      access_token_key=OAUTH_TOKEN,
                      access_token_secret=OAUTH_TOKEN_SECRET)


print(api)
resp = api.GetTrendsWoeid(US_WOE_ID)
for trend in resp:
    tweet= api.PostUpdate('.@samuelmoore Have you heard about {0}?'.format(trend._json['name']))
    print (tweet)


print('done')
