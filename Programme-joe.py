import urllib2
import json
url = "http://dev.c0l.in:9999/"
response = urllib2.urlopen(url).read()
data = json.loads(response.decode('utf8'))

# Get the list of valid sectors
listofsectors=[]
for record in data:
    recordSector = record["sector"]
listofsectors.append[recordSector]

#sector = raw_input("Choose a sector:\n")

#while sector != listofsectors:
 #   sector = raw_input("please choose a valid sector")
#else:
 #   print "found"
                    


   
         




        
