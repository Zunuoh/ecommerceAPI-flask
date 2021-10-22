from enum import unique
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
import routeServices
from dbInit import dbInit
from maInit import maInit

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def get():
    return jsonify({"msg":"hi"})

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///' + os.path.join(basedir,'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

dbInit(app)
maInit(app)



# ADD ITEM TO STORE
@app.route('/item', methods = ['POST'])
def addItem():
    return routeServices.createItem()

@app.route('/item', methods = ['GET'])
def getAllIems():
    return routeServices.getAllItems()

@app.route('/item/<id>', methods = ['GET'])
def getItem(id):
    return routeServices.getItem(id)

@app.route('/item/<id>', methods = ['PUT'])
def updateItem(id):
    return routeServices.updateItem(id)

@app.route('/item/<id>', methods =['DELETE'])
def deleteItem(id):
    return routeServices.deleteItem(id)


    

















if __name__ == '__main__':
    app.run(debug=True)