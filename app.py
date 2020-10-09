from flask import Flask,render_template,redirect,request,session,flash,url_for,g
import datetime
import sys
import random
import time

import json

import database_emp

app = Flask(__name__)


app.secret_key="dst5wukhsyurshjmuxy987"

#updating data usign MongoDb id obj
database_emp.update_emplyoee_details_mongo_id()

#updating data usign user id 
database_emp.update_emplyoee_details_user_id()

#updating multiple data usign user id 
database_emp.update_multiple_emplyoee_details_user_id()

#updating multiple data usign mongo id  obj
database_emp.update_multiple_emplyoee_details_mongo_id()

#deleting a field from a specific record 
database_emp.delete_a_field()

#deleting a record  using mongo id  obj
database_emp.delete_one_emplyoee_record_mongo_id()

#Its the entry point to the browser
@app.route("/")
def index():
	#get all data from db
	empinfo = database_emp.get_emplyoee_details()
	empdetailslist = []
	for e in empinfo:
		empdetailslist.append(e)
	return render_template('index.html', emplist = empdetailslist )


@app.route("/", methods=['POST'])
def update_emp_record():
	empdata = {}
	e_id = request.form['e_id']
	name = request.form['uname']
	designation = request.form['desig']
	phone_num = request.form['phone_num']
	address = request.form['address']
	email = request.form['email']
	#send data to db
	empdata["e_id"] = e_id
	empdata["name"] = name
	empdata["designation"] = designation
	empdata["phone_num"] = phone_num
	empdata["address"] = address
	empdata["email"] = email
	print (empdata)
	database_emp.save_emplyoee_details(empdata)
	return redirect(url_for('index'))
"""

@app.route("/<update/<emp_id>", methods = ['POST'])
def up_to_date():
	empid = emp_id
	database_emp.update_emplyoee_details(empid)
	return redirect(url_for('index'))



@app.route("/delete/<emp_id>", methods=['POST'])
def deleteRecord(emp_id):
    empid = emp_id
    emp_db.delete_record(empid)
    return redirect(url_for('index'))

"""

if __name__ == '__main__':
	app.run(debug=True)