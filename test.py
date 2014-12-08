import urllib2
import json
url = "http://dev.c0l.in:9999/"
response = urllib2.urlopen(url).read()
data = json.loads(response.decode('utf8'))
print data 
