from flask import request, jsonify
from dbInit import db
from models import Item, ItemSchema, item_schema, items_schema
from sqlalchemy.exc import IntegrityError, StatementError
from apiResponse import ApiResponseSchema, ApiResponse, SUCCESS,FAILURE,NOT_FOUND, api_response_schema, handleResponse

def createItem():
    try:
        name = request.json['name']
        descr = request.json['descr']
        price = request.json['price']
        qty = request.json['qty']
    
    except KeyError as keyerror:
        return f"{keyerror} not provided"

    newItem = Item(name, descr, price, qty)
    db.session.add(newItem)
    try:
        db.session.commit()
    except IntegrityError as ie:
        print(ie)
        return "Item creation failed"

    return handleResponse("New item created", item_schema.dump(newItem), SUCCESS, 200)

def getAllItems():
    allItems = Item.query.all()
    result = items_schema.dump(allItems)
    print(result)
    return handleResponse("All items", result, SUCCESS, 200)

def getItem(id):
    item = Item.query.get(id)
    if item is None:
        return handleResponse("User doesn't exist", None, FAILURE, 404)
    return handleResponse("", item_schema.dump(item), SUCCESS, 200)

def updateItem(id):
    item = Item.query.get(id)
    if item is None:
        return handleResponse("user doesn't exist", None, FAILURE, 404)
    try:
        name = request.json['name']
        descr = request.json['descr']
        price = request.json['price']
        qty = request.json['qty']
    except KeyError as keyerr:
        return f"{keyerr} not provided"

    item.name = name
    item.desc = descr
    item.price = price
    item.qty = qty

    db.session.commit()

    return handleResponse("Item updated", item_schema.dump(item), SUCCESS,200)

def deleteItem(id):
    item = Item.query.get(id)
    if item is None:
        return handleResponse("User doesn't exist", None, FAILURE, 404)
    db.session.delete(item)
    db.session.commit()
    return handleResponse("Wallet deleted", None, SUCCESS, 200)
    
       