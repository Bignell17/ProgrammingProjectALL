import urllib2
import json
url = "http://dev.c0l.in:8888/"
response = urllib2.urlopen(url).read()
data = json.loads(response.decode('utf8'))

Listofsectors = ["financial", "industrial goods", "healthcare", "services", "basic materials", "technology", "consumer goods", "utilities"]

user_input = raw_input("Choose a sector:\n")



        
