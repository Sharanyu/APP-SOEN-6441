from models import employee
from flask import *
import sqlite3
import sys

class DBController():
    def __int__(self):
        pass

    def find(self,table_name,fetchall=False,params=None):
        query = 'SELECT * FROM '+table_name
        self.cur.execute(query)
        result = self.cur.fetchall()
        return result

    def find_emp(self,id):
        self.con = sqlite3.connect("nyc.db")
        self.con.row_factory = sqlite3.Row
        self.cur = self.con.cursor()
        form_query = id
        self.cur.execute("select employee_id,employee_name FROM employee where employee_id =" + form_query)
        rows = self.cur.fetchall()
        return rows

    def view_emp(self):
        self.con = sqlite3.connect("nyc.db")
        self.con.row_factory = sqlite3.Row
        self.cur = self.con.cursor()
        self.cur.execute(
            "select employee.employee_id,employee_name,work_location_borough,base_salary_USD from employee INNER JOIN employee_details ON employee.employee_id=employee_details.employee_id limit 5")
        rows = self.cur.fetchall()
        return rows
