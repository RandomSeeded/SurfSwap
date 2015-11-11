# This file searches craigslist for surfboards, and saves the results to a database.

from lxml import html
import requests
from flask.ext.sqlalchemy import SQLAlchemy
import server

# server.import_test()

regions = [ 
    'bakersfield',
    'chico',
    'fresno',
    'goldcountry',
    'hanford',
    'humboldt',
    'imperial',
    'inlandempire',
    'losangeles',
    'mendocino',
    'merced',
    'modesto',
    'monterey',
    'orangecounty',
    'palmsprings',
    'redding',
    'sacramento',
    'sandiego',
    'sfbay',
    'slo',
    'santabarbara',
    'santamaria',
    'siskiyou',
    'stockton',
    'susanville',
    'ventura',
    'visalia',
    'yubasutter'
    ]

class Listing:
    def __init__(self, id, href, text, price):
        self.id = id
        self.href = href
        self.text = text
        self.price = price
    def __repr__(self):
        return self.id + ": "+ self.href + " - " + self.text + " - " + str(self.price)

def generate_listings(region):
    page = requests.get('http://' + region + '.craigslist.org/search/spo?sort=rel&query=surfboards')
    if page.status_code != 200:
        print('something went wrong')

    else:
        # This version looks at the rows
        tree = html.fromstring(page.content)
        rows = tree.xpath('//p[@class="row"]')
        listings = []
        for i in range(0, len(rows)):
            row = rows[i]
            listing_id = row.get('data-pid')
            priceSpan = row.find('a/span')
            price = priceSpan.text if priceSpan != None else '$0'
            anchor = row.find('span/span[@class="pl"]/a')
            link = anchor.get('href')
            text = anchor.text
            listing = Listing(listing_id, link, text, price)
            listings.append(listing)
        
        return listings

for i in range(0, len(regions)):
    listings = generate_listings(regions[i])
    # print(listings)







