from bs4 import BeautifulSoup
import requests

source = requests.get("https://revenue.delaware.gov/business-license-search/?bname&activity=RETAILER-GROCERY"
                      "+SUPERMARKET&address_1&city=WILMINGTON&state&zip").text
soup = BeautifulSoup(source, features="html.parser")

# markets = soup.find('div', {'class': 'col-md-3 topicBlock'})
markets = soup.find('div', {'id': 'filter-content'})
markets_list = markets.find_all('div', 'col-md-3 topicBlock')

for markets in markets_list:
    names = markets.find('h3').contents[0]
    x = markets.find_all('p')[-1].contents[0]
    details = x[11:]
    print(names)
    print(details)

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
