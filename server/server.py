from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/surfboard-listings.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost:3306/surfSwap'
db = SQLAlchemy(app)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()

