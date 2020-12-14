""" ============================================
; Title:  Assignment 9.3
; Author: Richard Krasso
; Date:   December 13, 2020
; Modified By: Juvenal Gonzalez
; Description: Update a user document in MongoDB and output the doucument
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
# updates users email by querying their employee_id and using the set function to update
db.users.update_one(

    {"employee_id": "0011238"},

    {

        "$set": {

            "email": "juvgonzalez@my365.bellevue.edu"

        }

    }

)
#pretty prints user document by querying their employe_id
pprint.pprint(db.users.find_one({"employee_id": "0011238"}))