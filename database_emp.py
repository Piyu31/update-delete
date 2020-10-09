from pymongo import MongoClient
import datetime
import sys

from bson.objectid import ObjectId

global con
global db
global col

def connect_db():
	global con
	global db
	global col
	con = MongoClient('mongodb+srv://test:test@cluster0.kw4id.mongodb.net/Employee?retryWrites=true&w=majority')
	db = con.Employee
	col = db.employee_records


def get_emplyoee_details():
	global col
	connect_db()
	emp_data_from_db = col.find({})
	return emp_data_from_db


def save_emplyoee_details(empinfo):
	global col
	connect_db()
	col.insert(empinfo)
	return



def update_emplyoee_details_mongo_id():
	global col
	connect_db()
	col.update_one({"_id":ObjectId('5f7ffc4820738b194a10d40b')}, {'$set' : {'name' : 'Justin' }})
	return

def update_emplyoee_details_user_id():
	global col
	connect_db()
	col.update_one({"e_id":"4537"}, {'$set' : {'name' : 'July' }})
	return


def update_multiple_emplyoee_details_mongo_id():
	global col
	connect_db()
	col.update(
    {
        "_id":
            {
                "$in":
                    [
                        ObjectId("5f7ffc4820738b194a10d40b"),
                        ObjectId("5f7fff2220738b194a10d40e")

                    ]
            }
    },
  
        {'$set' : {'Employee_type' : 'Trainee' }}

    )
	return

def update_multiple_emplyoee_details_user_id():
	global col
	connect_db()
	col.update(
    {
        "e_id":
            {
                "$in":
                    [
                        "8675",
                        "6087"

                    ]
            }
    },
    
        {'$set' : {'Employee_type' : 'Trainee' }}

    )
	return



def delete_one_emplyoee_record_mongo_id():
	global col
	connect_db()
	col.delete_one( {"_id": ObjectId("5f7ffc4820738b194a10d40b")});
	return

def delete_a_field():
	global col
	connect_db()
	col.update({"_id":ObjectId("5f7fff6220738b194a10d411")}, 
		{'$unset':{'Employee_type':'1'}});
	return


"""
 def update_emplyoee_details():
 	global col
 	connect_db()
 	myque = {"_id":ObjectId(empid), '$set':{'name':'Lighting Mcqueen'}}
 	col.update_one(myque)
 	return
"""

"""
def update_emplyoee_details_user_id():
	global col
	connect_db()
	myquer = {"e_id":"4537"}, {'$set' : {'name' : 'July' }}
	col.update_one(myquer)
	return

"""

"""
def delete_record(emp_id):
    global col
    connect_db()
    myquery = {"_id": ObjectId(emp_id)}
    col.delete_one(myquery)
    return
 """
