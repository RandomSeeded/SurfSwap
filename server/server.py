from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

@app.route("/")
def hello():
    return "Hello World!"

# This code was to check the syntax on referencing functions defined here in another file
# def import_test():
#     print('hi')

if __name__ == "__main__":
    app.run()

