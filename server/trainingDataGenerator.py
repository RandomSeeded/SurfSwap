from server import db
import listingModel

# Model for storing our training data (may need addl fields)
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    href = db.Column(db.String(80), unique=False)
    text = db.Column(db.String(128), unique=False)
    price = db.Column(db.String(10), unique=False)
    isSurfboard = db.Column(db.Boolean)

    def __init__(self, id, href, text, price, isSurfboard):
        self.id = id
        self.href = href
        self.text = text
        self.price = price
        self.isSurfboard = isSurfboard

db.create_all()

listings = listingModel.Listing.query.all()
for i in range(0, 0):
# for i in range(0, len(listings)):
    #print('hi')
    listing = listings[i]
    item = db.session.query(Item).get(listing.id)
    if item == None:
        print(listing)
        isSurfboard = ""
        while (isSurfboard != 'y' and isSurfboard != 'n'):
            isSurfboard = input("Is this a surfboard? Y/N").lower()
        isSurfboard = True if isSurfboard == "y" else False
        item = Item(listing.id, listing.href, listing.text, listing.price, isSurfboard)
        db.session.add(item)
        db.session.commit()

print(Item.query.all())

# print(listingModel.Listing.query.all())

