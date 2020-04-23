import json, csv, re

tweets = {}

i = 0

with open('tweets.json', encoding="utf8") as f:
    data = json.load(f)
    for tweet in data["tweets"]:
        i += 1
        id_tweet = tweet['id']
        text = tweet["text"]
        usernames = re.findall("@[a-zA-Z0-9_]{0,15}", text) # Look up for twitter usernames
        
        for p1 in range(len(usernames)):
            for p2 in range(p1 + 1, len(usernames)):
                user1 = usernames[p1].lower()
                user2 = usernames[p2].lower()
                pair = (user1, user2)
                pair2 = (user2, user1)
                if pair in tweets:
                    tweets[pair] += 1
                elif pair2 in tweets:
                    tweets[pair2] += 1
                else:
                    tweets[pair] = 1
print(i)

"""
numRTs = 10

with open('tweets_usernames10.csv', mode = 'w', encoding="utf8") as f:
    writer = csv.writer(f, delimiter=';', quotechar='"')
    writer.writerow(["Source", "Target", "Weight"])
    for (x, y), val in tweets.items():
        if val >= numRTs:
            writer.writerow([x, y, val])
            """