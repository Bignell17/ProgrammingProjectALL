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
    #decodes the url data into proper python arrays
    incomestatement.writerow([
        'Name',
        'Sales',
        'Interest Payable',
        'Expenses',
        'Interest Recivable',
        'Opening Stock',
        'Closing Stock'])
    #prints names the columns in excel doc
    
    selectsector = raw_input("please choose a sector:\n")
    for item in data:
        if item.get('sector', None) == selectsector:
            incomestatement.writerow([
            item['company']['name'],
            item['company']['sales'],
            item['company']['interest_payable'],
            item['company']['expenses'],
            item['company']['interest_receivable'],
            item['company']['opening_stock'],
            item['company']['closing_stock'],])
    print "Done"
    #prints the data in the excel doc 

