import sqlite3
import sys

from flask import *

from models.Employee import emp
from models.EmployeeDetails import empdetails

# from payrollreference import payroll
# from agency import agency


class DBController:
    def __init__(self):
        self.cur = None
        self.con = None

    def __int__(self):
        pass

    def find(self, table_name, fetchall=False, params=None):
        query = f"SELECT * FROM {table_name}"
        self.cur.execute(query)
        return self.cur.fetchall()

    def find_emp(self, id):
        self._db_connection()
        emp.set_emp_id(id)
        form_query = emp.get_emp_id()
        return self._execute_query(
            'SELECT employee.employee_id,employee_name,agency_name,fiscal_year,work_location_borough,title_description,work_hours,gross_salary_USD FROM employee JOIN employee_details ON employee.employee_id = employee_details.employee_id JOIN payroll_reference ON employee.employee_id = payroll_reference.employee_id JOIN agency ON payroll_reference.payroll_number = agency.payroll_number WHERE employee.employee_id ="{0}"',
            form_query,
            'SELECT employee.employee_id,employee_name,agency_name,fiscal_year,work_location_borough,title_description,work_hours,gross_salary_USD FROM employee JOIN employee_details ON employee.employee_id = employee_details.employee_id JOIN payroll_reference ON employee.employee_id = payroll_reference.employee_id JOIN agency ON payroll_reference.payroll_number = agency.payroll_number WHERE employee.employee_id ="{0}"',
        )

    def view_emp(self):
        self._db_connection()
        self.cur.execute(
            "select employee.employee_id,employee.employee_name,fiscal_year,work_location_borough,gross_salary_USD from employee INNER JOIN employee_details ON employee.employee_id=employee_details.employee_id limit 5"
        )
        return self.cur.fetchall()

    def view_emp_from(self, location):
        self._db_connection()
        empdetails.set_location(location)
        form_query = empdetails.get_location()
        return self._execute_query(
            'select employee.employee_id,employee_name from employee INNER JOIN employee_details on employee.employee_id=employee_details.employee_id WHERE work_location_borough="{0}"',
            form_query,
            'select employee.employee_id,employee_name,fiscal_year from employee join employee_details on employee.employee_id=employee_details.employee_id where work_location_borough="{0}"',
        )

    def top_5_earners(self, fiscal_year):
        self._db_connection()
        empdetails.set_fiscal_year(fiscal_year)
        form_query = empdetails.get_fiscal_year()
        return self._execute_query(
            "select employee_id, employee_name, gross_salary_USD from employee join employee_details on employee.employee_id = employee_details.employee_id where fiscal_year = {0} order by gross_salary_USD desc limit 5",
            form_query,
            "select employee_id, employee_name, gross_salary_USD from employee join employee_details on employee.employee_id = employee_details.employee_id where fiscal_year = {0} order by gross_salary_USD desc limit 5",
        )

    # TODO Rename this here and in `find_emp`, `view_emp`, `view_emp_from` and `top_5_earners`
    def _execute_query(self, arg0, form_query, arg2):
        print(arg0.format(form_query))
        self.cur.execute(arg2.format(form_query))
        return self.cur.fetchall()

    # TODO Rename this here and in `find_emp`, `view_emp`, `view_emp_from` and `top_5_earners`
    def _db_connection(self):
        self.con = sqlite3.connect("nyc.db")
        self.con.row_factory = sqlite3.Row
        self.cur = self.con.cursor()
