# This file searches craigslist for surfboards, and saves the results to a database.

from flask.ext.sqlalchemy import SQLAlchemy
from server import db
import listingModel

regions = [ 
    'bakersfield',
    # 'chico',
    # 'fresno',
    # 'goldcountry',
    # 'hanford',
    # 'humboldt',
    # 'imperial',
    # 'inlandempire',
    # 'losangeles',
    # 'mendocino',
    # 'merced',
    # 'modesto',
    # 'monterey',
    # 'orangecounty',
    # 'palmsprings',
    # 'redding',
    # 'sacramento',
    # 'sandiego',
    # 'sfbay',
    # 'slo',
    # 'santabarbara',
    # 'santamaria',
    # 'siskiyou',
    # 'stockton',
    # 'susanville',
    # 'ventura',
    # 'visalia',
    # 'yubasutter'
    ]

db.create_all()

for i in range(0, len(regions)):
    print('Retrieving listings for',regions[i],'...')
    listings = listingModel.generate_listings(regions[i])

print(listingModel.Listing.query.all())

