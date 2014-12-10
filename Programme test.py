print "Welcome to our program"
print "Getting information on different sectors\n"

password = input("Please enter password: ")

if password == "sector":
    print ("You are in our program")
    




import urllib2
import json
url = "http://dev.c0l.in:9999/"
response = urllib2.urlopen(url).read()
data = json.loads(response.decode('utf8'))

listofsectors = ("financial", "industrial goods", "healthcare", "services", "basic materials", "technology", "consumer goods", "utilities")
found = False
user_input = raw_input("Select a sector: ")

while sector in listofsectors:
    if user_input == sector:
        print "found"
        found = True
    if found == False:
        print "Unlucky"
    

    
