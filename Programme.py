import urllib2
import json
url = "http://dev.c0l.in:9999/"
response = urllib2.urlopen(url).read()
data = json.loads(response.decode('utf8'))

listofsectors = ["financial", "industrial goods", "healthcare", "services", "basic materials", "technology", "consumer goods", "utilities"]

user_input = raw_input("Choose a sector:\n")
while user_input != listofsectors:
    user_input = raw_input("Choose a sector:\n")
else:
    print "found"



        
