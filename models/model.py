# importing required libraries
import sqlite3

# importing objects of tables
from models.employee import emp
from models.employeedetails import empdetails

# DBController class is the main component of Model component of MVC architecture.
class DBController:
    def __init__(self):
        self.cur = None
        self.con = None

    def __int__(self):
        pass

    # defining a function which accepts a id from the user and uses the data mapper object to fetch details from the database about the employuee_id.
    def find_emp(self, id):
        self._db_connection()
        emp.set_emp_id(id)
        form_query = emp.get_emp_id()
        return self._execute_query(
            'SELECT employee.employee_id,employee_name,agency_name,fiscal_year,work_location_borough,title_description,work_hours,gross_salary_USD FROM employee JOIN employee_details ON employee.employee_id = employee_details.employee_id JOIN payroll_reference ON employee.employee_id = payroll_reference.employee_id JOIN agency ON payroll_reference.payroll_number = agency.payroll_number WHERE employee.employee_id ="{0}"',
            form_query,
            'SELECT employee.employee_id,employee_name,agency_name,fiscal_year,work_location_borough,title_description,work_hours,gross_salary_USD FROM employee JOIN employee_details ON employee.employee_id = employee_details.employee_id JOIN payroll_reference ON employee.employee_id = payroll_reference.employee_id JOIN agency ON payroll_reference.payroll_number = agency.payroll_number WHERE employee.employee_id ="{0}"',
        )

    # defining a function which display 5 records from the database.
    def view_emp(self):
        self._db_connection()
        self.cur.execute(
            "select employee.employee_id,employee.employee_name,fiscal_year,work_location_borough,gross_salary_USD from employee INNER JOIN employee_details ON employee.employee_id=employee_details.employee_id limit 200"
        )
        return self.cur.fetchall()

    # defining a function which accepts a location from the user and uses the data mapper object to fetch details from the database about the location.
    def view_emp_from(self, location):
        self._db_connection()
        empdetails.set_location(location)
        form_query = empdetails.get_location()
        return self._execute_query(
            'select employee.employee_id,employee_name from employee INNER JOIN employee_details on employee.employee_id=employee_details.employee_id WHERE work_location_borough="{0}"',
            form_query,
            'select employee.employee_id,employee_name,fiscal_year from employee join employee_details on employee.employee_id=employee_details.employee_id where work_location_borough="{0}"',
        )

    # defining a function which accepts a year from the user and uses the data mapper object to fetch details from the database about the fiscal_year.
    def top_5_earners(self, fiscal_year):
        self._db_connection()
        empdetails.set_fiscal_year(fiscal_year)
        form_query = empdetails.get_fiscal_year()
        return self._execute_query(
            "select employee.employee_id, employee_name, gross_salary_USD from employee join employee_details on employee.employee_id = employee_details.employee_id where fiscal_year = {0} order by gross_salary_USD desc limit 5",
            form_query,
            "select employee.employee_id, employee_name, gross_salary_USD from employee join employee_details on employee.employee_id = employee_details.employee_id where fiscal_year = {0} order by gross_salary_USD desc limit 5",
        )

    # defining a helper function to call execute and fetch methods. This will reduce redundant code and improve code readability
    def _execute_query(self, arg0, form_query, arg2):
        print(arg0.format(form_query))
        self.cur.execute(arg2.format(form_query))
        return self.cur.fetchall()

    # defining a helper function to call establish db connection. This will reduce redundant code and improve code readability
    def _db_connection(self):
        self.con = sqlite3.connect("database/NYC_payroll_data.db")
        self.con.row_factory = sqlite3.Row
        self.cur = self.con.cursor()
dbc = DBController()