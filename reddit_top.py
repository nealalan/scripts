import urllib.request
import json
url = 'http://www.reddit.com/r/all/top/.json'
req = urllib.request.Request(url)

##parsing response
r = urllib.request.urlopen(req).read()
cont = json.loads(r.decode('utf-8'))
counter = 0

##parcing json
for item in cont['data']['children']:
    counter += 1
    print("Title:", item['data']['title'], "\nComments:", item['data']['num_comments'])
    print("----")


##parcing json cols
#print("Count    ")
#for item in cont['data']['children']:
#    counter += 1
#    print(item['data']['num_comments'], "  ",item['data']['title'])

##print formated
#print (json.dumps(cont, indent=4, sort_keys=True))
#print("Number of titles: ", counter)

#print(cont)
