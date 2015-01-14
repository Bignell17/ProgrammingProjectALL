import urllib2
import json
url = "http://dev.c0l.in:9999/"
response = urllib2.urlopen(url).read()
data = json.loads(response.decode('utf8'))

#financial, services, industrial goods, basic materials, consumer goods, technology, healthcare

#user chooses a sector

selectsector = raw_input("please choose a sector:\n")

for record in data:
    if record["sector"] == selectsector:
        print "company found"




        

