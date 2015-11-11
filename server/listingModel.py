from server import db
import requests
from lxml import html

class Listing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    href = db.Column(db.String(80), unique=False)
    text = db.Column(db.String(128), unique=False)
    price = db.Column(db.String(10), unique=False)

    def __init__(self, id, href, text, price):
        self.id = id
        self.href = href
        self.text = text
        self.price = price
    def __repr__(self):
        return str(self.id) + ": "+ self.href + " - " + self.text + " - " + str(self.price)

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

            # Generates the variables we want to store
            price = priceSpan.text if priceSpan != None else '$0'
            anchor = row.find('span/span[@class="pl"]/a')
            link = anchor.get('href')
            text = anchor.text
            listing = Listing(listing_id, link, text, price)
            listings.append(listing)

            # Adds to database if not already stored
            alreadyListed = db.session.query(Listing).get(listing_id)
            if (alreadyListed == None):
                db.session.add(listing)
                db.session.commit()
        
        return listings
