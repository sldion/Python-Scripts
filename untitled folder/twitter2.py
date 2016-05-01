import twitter

api = twitter.Api(consumer_key='X56t9CLmLYu2ZLfQR4QHSrwch',
        consumer_secret='lE1Hg13m4xPiaU1NNZmqrUaUUFcyd3FzWfE3UWngsoTezLM3NT',
        access_token_key='543690533-9Xf1g4IwA2dMCxKA225ZQkD33gTjxZcotva5FAc6',
        access_token_secret='0WREDuqpUPzlXgq1FIQjS1BprR0xBaRsnszmYy9V6H6nv')

statuses = api.GetUserTimeline(screen_name='kanyewest', count=200)# exclude_replies=True)

# class twitterCalls:
#
#     def getTweets(self,)
