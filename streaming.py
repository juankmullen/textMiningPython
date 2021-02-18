import json
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
ckey = 'QqySEZSnUKkhHgNFJkSsXbXaF'
csecret = '4wD1mwlAHx20MqS8dE5vmUYs1rVKmOUoj1WN2XUItBJVXGjb68'
atoken = '1132026149700341762-pl9MPDEFZeqFFCjfUdg0C94ibYrhvV'
asecret = '8cT7AMfiK0RNKz5gHRwbv6HsVXIqU6pRj5ExvqeOPmqX9'


csvFile = open('test.csv', 'a')

class listener(StreamListener):
    def on_data(self, data):
        # La API de Twitter devuelve datos en formato JSON, asi que hay que decodificarlos.
        try:
            decoded = json.loads(data)
        except Exception as e:
            print(e) #no queremos que el script se pare
        return True
        if decoded.get('geo') is not None:
            location = decoded.get('geo').get('coordinates')
        else:
            location = '[,]'
        text = decoded['text'].replace('\n',' ')
        user = '@' + decoded.get('user').get('screen_name')
        created = decoded.get('created_at')
        tweet = '%s|%s|%s|s\n' % (user,location,created,text)
        csvFile.write(tweet)
        print(tweet)
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    print('Empezando...')
    auth = OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret)
    twitterStream = Stream(auth, listener())
    twitterStream.filter(track=["#tomas"])