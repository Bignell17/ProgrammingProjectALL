import urllib2
import json
import csv
finpos = csv.writer(open("financial position output.csv", "wb"))
#this opens the financial position output file and makes it writable.

incomestatement = csv.writer(open("income position output.csv", "wb"))
#this opens the income statement output file and makes that wb

def income_statement():
    url = "http://dev.c0l.in:8888/"
    response = urllib2.urlopen(url).read()
    data = json.loads(response.decode('utf8'))
    #decodes the url data into python
    incomestatement.writerow([
        'Name',
        'Sales',
        'Interest Payable',
        'Expenses',
        'Interest Recivable',
        'Opening Stock',
        'Closing Stock'])
    #names the columns in the excel document
