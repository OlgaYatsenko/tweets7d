import urllib.request, urllib.parse, urllib.error
import twurl #Oathhandling,the reference ti hidden.file
import json
import ssl


# Request Tweets from last 7 days

TWITTER_URL ="https://api.twitter.com/1.1/search/tweets.json"

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

word=input("Enter what you want to find: ")

params={}
params['q']=word
params['result_type']='recent'
url = twurl.augment(TWITTER_URL,params)
print('Retrieving', url)
connection = urllib.request.urlopen(url, context=ctx)
data = connection.read().decode()

py1 = json.loads(data) #data in python

#write into file
r=open("results.txt","w+")
r.truncate()
r.write(json.dumps(py1, indent=2))#data in json
r.close()


for user in py1['statuses']:
    print ("USER: ", user["id_str"],"STATUS: ", user['text'])
    try:
       link=user["retweeted_status"]['entities']['urls'][0]['url']
    except (IndexError,KeyError):
       try:
           link=user['user']['entities']['url']['urls'][0]['url']
       except (IndexError,KeyError):
           link='JUST STATUS, NO LINKS'
    print (link)

headers = dict(connection.getheaders())
print ("=======HEADERS======")
#print (headers)
print('Remaining', headers['x-rate-limit-remaining'])


