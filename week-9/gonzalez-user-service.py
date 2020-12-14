""" ============================================
; Title:  Assignment 9.2
; Author: Richard Krasso
; Date:   December 13, 2020
; Modified By: Juvenal Gonzalez
; Description: Insert a user document into the MongoDB and output the doucument
;=========================================== """
# imports MongoClient which allows server connection with MongoD
from pymongo import MongoClient
#pretty print
import pprint
#UTC function package
import datetime
#initializes connection do database
client = MongoClient('localhost', 27017)
#specifies the db in a db variable
db = client.web335
# user document with required fields
user = {
    "first_name": "Python",

    "last_name": "Mongo",

    "email": "pymongo@gmail.com",

    "employee_id": "0011238",

    "date_created": datetime.datetime.utcnow()
}
# inserts user document into db and passes _id field into user_id variable
user_id = db.users.insert_one(user).inserted_id
#prints user_id
print(user_id)
#pretty prints user by querying the users employee_id
pprint.pprint(db.users.find_one({"employee_id": "0011238"}))