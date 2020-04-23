import json, csv, secrets

tweets = {}
i = 0

with open('tweets.json', encoding="utf8") as f:
    data = json.load(f)
    for tweet in data["tweets"]:
        i += 1
        id_tweet = tweet['id']
        idRT = ''
        if "retweeted_status_id" in tweet:
            idRT = tweet["retweeted_status_id"]
        text = tweet["text"]
        if idRT not in tweets:
            tweets[idRT] = []
        tweets[idRT].append((id_tweet, text)) # Key = RT id, Value = (tweet id, tweet)
        
secure = secrets.SystemRandom()
print(i)

#leaders = ["RT @toret", "RT @AdaColau", "RT @AlfredBosch", "RT @MJLecha", "RT @CarinaMejias", "RT @xaviertrias", "RT @albertofdezxbcn", "RT @jaumecollboni"]
leaders = ["RT @albertofdezxbcn"]
"""
nums = len(tweets) // 2
list_random = secure.sample(tweets.keys(), nums)
with open('tweets.csv', mode = 'w') as f:
    writer = csv.writer(f, delimiter=',', quotechar='"')
    writer.writerow(["Source", "Target"])
    for tweet in list_random:
        writer.writerow([tweet, tweets[tweet]])
"""
"""
list_text = []

with open('tweets_albertofdezxbcn.csv', mode = 'w', encoding="utf8") as f:
    writer = csv.writer(f, delimiter=';', quotechar='"')
    #writer.writerow(["Source", "Target", "Tweet"])
    writer.writerow(["Tweet"])
    for idtweet, (idRT, text) in tweets.items():
        #if text.startswith(tuple(leaders)):
            #if text not in list_text:
                writer.writerow([idRT, text])
                #list_text.append(text)
"""

numRTs = 10

with open('tweets_filtered.csv', mode = 'w', encoding="utf8") as f:
    writer = csv.writer(f, delimiter=';', quotechar='"')
    writer.writerow(["Source", "Target", "Tweet"])
    for idRT, elems in tweets.items():
        if idRT != '' and len(elems) >= numRTs:
            #print(idRT, len(elems))
            for (idtweet, tweet) in elems:
                writer.writerow([idtweet, idRT, tweet])