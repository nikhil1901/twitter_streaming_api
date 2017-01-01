from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

ckey = 'IN4kGzR8g7eLWkeJgFMiZC028'
csecret = '3JyC1h55a0EkrxiqcmBZ7FVe8s9BEZQL3GuXZvfDoTBUI3g0hx'
atoken = '132133252-9nLVqmslBT5UHuqDamddjCtR8J1x6hMdlXQI8Pb2'
asecret = 'a6Y1YZ1hrhuhR7Y9cjyt8ojqVw2IC5vrLKPBx5m12Nvjt'

class listener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["sherlock"])
