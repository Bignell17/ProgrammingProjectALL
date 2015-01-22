import urllib2
import json
import csv
finpos = csv.writer(open("financial position output.csv", "wb"))
#this opens the financial position output file and makes it writable.

incomestatement = csv.writer(open("income position output.csv", "wb"))
#this opens the income statement output file and makes that wb
