'''
Local Settings for a heroku_ebooks account. #fill in the name of the account you're tweeting from here.
'''

#configuration
MY_CONSUMER_KEY = 'AJPXDsJ4O4FYUletYZ0UzMeQV'
MY_CONSUMER_SECRET = 'KGm5zr25iOfbbwlZbtUK4oEwPq9PKw7KCaQCiLF6nZyP00dskd'
MY_ACCESS_TOKEN_KEY = '822493022860574723-DLaHanWhRyX1JxbwJZKVac45FebnqPM'
MY_ACCESS_TOKEN_SECRET = 'dE8tLlePWmchmN2fG3KoQhuiOo3sxEfrv30hwl6P05iZv'

SOURCE_ACCOUNTS = ["vaiIagay"] #A list of comma-separated, quote-enclosed Twitter handles of account that you'll generate tweets based on. It should look like ["account1", "account2"]. If you want just one account, no comma needed.
ODDS = 1 #How often do you want this to run? 1/8 times?
ORDER = 2 #how closely do you want this to hew to sensical? 1 is low and 3 is high.
DEBUG = True #Set this to False to start Tweeting live
STATIC_TEST = False #Set this to True if you want to test Markov generation from a static file instead of the API.
TEST_SOURCE = ".txt" #The name of a text file of a string-ified list for testing. To avoid unnecessarily hitting Twitter API. You can use the included testcorpus.txt, if needed.
TWEET_ACCOUNT = "vailagay_ebooks" #The name of the account you're tweeting to.
