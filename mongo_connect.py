from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME']= 'mydb'
app.config['MONGO_URI']='mongodb://avi:qwerty1@ds137370.mlab.com:37370/mydb'

mongo = PyMongo(app)

@app.route('/add')

def add():
    user = mongo.db.users
    user.insert({'name':'Anthony'})
    return 'Added User'

if __name__ == '__main__':
    app.run(debug=True)
