from bs4 import BeautifulSoup
import requests
import csv

URL = "https://revenue.delaware.gov/business-license-search/page/4" \
      "/?bname&activity=RETAILER-FOOD%20%28EXCEPT%20RESTAURANT%29&address_1&city=WILMINGTON&state&zip"
source = requests.get(URL).text
soup = BeautifulSoup(source, features="html.parser")

# markets = soup.find('div', {'class': 'col-md-3 topicBlock'})
market = soup.find('div', {'id': 'filter-content'})
market_list = market.find_all('div', 'col-md-3 topicBlock')

for market in market_list:
    names = market.find('h3').contents[0]
    x = market.find_all('p')[-1].contents[0]
    details = x[11:]
    y = market.find_all('p')[1].contents[0]
    activity = y[20:]
    with open('fridge.csv', mode='a', newline='\n') as fridge:
        store_writer = csv.writer(fridge, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        store_writer.writerow([names, details, activity])
    print(names + "," + details + "," + activity)

'''
<div id="filter-content">
    <div class="col-md-3 topicBlock">
        <div class="name"> 
        <h3>ADAMS MARKET LLC </h3><br>								 
    </div>
    <div class="detail">
        <p>License Number : 1999209124</p>
        <p>Business Activity : RETAILER-GROCERY SUPERMARKET</p>
        <p>Valid From : 01-01-2019</p>
        <p>Valid To : 12-31-2021</p>
        <p>Location : 800 W 4TH ST STE 201, WILMINGTON, DE 19801</p>
'''
