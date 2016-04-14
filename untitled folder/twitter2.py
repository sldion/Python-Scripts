import twitter

api = twitter.Api(consumer_key='PvfC9xdwuGNBWyG4RHothCUIG', consumer_secret='DRzGRjI8UehRkzcBA0MTuouSPl8aNTNDCj39kif0G8Rl3KUdyV', access_token_key='333001911-KHFQmDGyzFsLoNofxhrzBkmYPn7mBvh7Qsh09EPg', access_token_secret='k5lpPdopcV5hbqUa7Y6HAQfVPbfZcugGmDC7Tl4YT256h')


status = api.GetUserTimeline(screen_name = 'kanyewest', count = 1000)



kanyeWestFile = open('kanyeWest.txt', 'w')


for s in status:
    kanyeWestFile.write(s.text.encode('utf8') + '\n')

kanyeWestFile.close
