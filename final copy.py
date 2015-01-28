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
        'Closing Stock',
        'Cost of Sales',
        'gross profit',
        'net profit',
        'profit for the period',])
    #prints names the columns in excel doc
    
    selectsector = raw_input("please choose a sector:\n")
    for item in data:
        cost_of_sales = item['company']['opening_stock'] - item['company']['expenses'] - item['company']['closing_stock']
        gross_profit = item['company']['sales'] - cost_of_sales
        net_profit = item['company']['expenses'] - gross_profit
        profit_for_the_period = item['company']['interest_payable'] + item['company']['interest_receivable'] - net_profit
        #these are the equations for the maths behind. these also have to be rearranged in order.



        if item.get('sector', None) == selectsector:
            incomestatement.writerow([
            item['company']['name'],
            item['company']['sales'],
            item['company']['interest_payable'],
            item['company']['expenses'],
            item['company']['interest_receivable'],
            item['company']['opening_stock'],
            item['company']['closing_stock'],
            gross_profit,
            cost_of_sales,
            net_profit,
            profit_for_the_period])
    print "Saving complete. Please open the correct CSV file"
    #prints the data in the excel doc 




def financial_position():
    url = "http://dev.c0l.in:9999/"
    response = urllib2.urlopen(url).read()
    data = json.loads(response.decode('utf8'))
    #decodes the url data into proper python arrays
    finpos.writerow([
        'Name',
        'current liabilities',
        'current assets',
        'non current liabilities',
        'equity',
        'non current assets',
        'total assets',
        'total equity & liabilities'])
    #prints names the columns in excel doc
    
    
    selectsector = raw_input("please choose a sector:\n")
    for item in data:
        total_assets = item['company']['current_assets'] + item['company']['non_current_assets']
        total_equity_liabilities = item['company']['non_current_liabilities'] +item['company']['current_liabilities'] + item['company']['equity'] 

        if item.get('sector', None) == selectsector:
            finpos.writerow([
            item['company']['name'],
            item['company']['current_liabilities'],
            item['company']['current_assets'],
            item['company']['non_current_liabilities'],
            item['company']['equity'],
            item['company']['non_current_assets'],
            total_assets,
            total_equity_liabilities])
    print "Saving complete. Please open the correct CSV file"
    #print out the data in the excel document

question= raw_input ("choose a statement: ")
#this prompts the user to choose a financial statement

if question == "income statement":
    income_statement()
elif question== "financial position":
    financial_position()
#this determines which statement to execute







 #financial, services, industrial goods, basic materials, consumer goods, technology, healthcare

#user chooses a sector        
