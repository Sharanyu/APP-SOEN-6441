import sqlite3
import pandas as pd
from configClass import config

class LoadData:
    def __init__(self):
        self.configObj = config()
        self.configdf = self.configObj.readConfig()
    def createEmployeeTable(self,database):
        try:
            database= self.configObj.getDatabase(self.configdf)
            sqliteConnection = sqlite3.connect(database)
            cursor = sqliteConnection.cursor()
            create_table_query = '''CREATE TABLE IF NOT EXISTS employee (employee_id INT PRIMARY KEY,employee_name TEXT NOT NULL UNIQUE);'''
            cursor = sqliteConnection.cursor()
            print("Successfully Connected to SQLite")
            cursor.execute(create_table_query)
            sqliteConnection.commit()
            print("SQLite table Employee created")
        except sqlite3.Error as error:
            print("Error while creating a sqlite table :", error)
            cursor.close()
            
    def createEmployeeDetailsTable(self,database):
        try:
            database= self.configObj.getDatabase(self.configdf)
            sqliteConnection = sqlite3.connect(database)
            cursor = sqliteConnection.cursor()
            create_table_query = '''CREATE TABLE IF NOT EXISTS employee_details (employee_id INT PRIMARY KEY,title_description TEXT,work_location_borough TEXT,fiscal_year INT,pay_basis TEXT,base_salary_USD REAL,work_hours REAL, gross_salary_USD REAL, overtime_hours REAL,overtime_commission_USD REAL, other_pay_USD REAL);'''
            cursor = sqliteConnection.cursor()
            cursor.execute(create_table_query)
            sqliteConnection.commit()
            print("SQLite table EmployeeDetails created")
        except sqlite3.Error as error:
            print("Error while creating a sqlite table :", error)
            cursor.close()
            
    def createPayrollTable(self,database):
        try:
            database= self.configObj.getDatabase(self.configdf)
            sqliteConnection = sqlite3.connect(database)
            cursor = sqliteConnection.cursor()
            create_table_query = '''CREATE TABLE IF NOT EXISTS payroll_reference (payroll_number INT,employee_id INT PRIMARY KEY);'''
            cursor = sqliteConnection.cursor()
            cursor.execute(create_table_query)
            sqliteConnection.commit()
            print("SQLite table Payroll created")
        except sqlite3.Error as error:
            print("Error while creating a sqlite table :", error)
            cursor.close()
            
    def createAgencyTable(self,database):
        try:
            database= self.configObj.getDatabase(self.configdf)
            sqliteConnection = sqlite3.connect(database)
            cursor = sqliteConnection.cursor()
            create_table_query = '''CREATE TABLE IF NOT EXISTS agency (payroll_number INT PRIMARY KEY,agency_name TEXT NOT NULL UNIQUE);'''
            cursor = sqliteConnection.cursor()
            cursor.execute(create_table_query)
            sqliteConnection.commit()
            print("SQLite table Agency created")
        except sqlite3.Error as error:
            print("Error while creating a sqlite table :", error)
    
    def writeTable(self,database,agency,employee,employee_details,payroll_reference):
        database= self.configObj.getDatabase(self.configdf)
        sqliteConnection = sqlite3.connect(database)
        cur = sqliteConnection.cursor()
        try:
            agency.to_sql('agency', sqliteConnection, if_exists='replace', index=False)
            pd.read_sql('select * from agency', sqliteConnection)
        except sqlite3.Error as error:
            print("Error while uploading agency table data", error)
  
        try:
            employee.to_sql('employee', sqliteConnection, if_exists='replace', index=False)
            pd.read_sql('select * from employee', sqliteConnection)
        except sqlite3.Error as error:
            print("Error while uploading employee table data", error)
 
        try:
            payroll_reference.to_sql('payroll_reference', sqliteConnection, if_exists='replace', index=False) # - writes the pd.df to SQLIte DB
            pd.read_sql('select * from payroll_reference', sqliteConnection)
        except sqlite3.Error as error:
            print("Error while uploading payroll table data", error)
            
        try:
            employee_details.to_sql('employee_details', sqliteConnection, if_exists='replace', index=False) # - writes the pd.df to SQLIte DB
            pd.read_sql('select * from employee_details', sqliteConnection)
        except sqlite3.Error as error:
            print("Error while uploading employee_details table data", error)
    
        sqliteConnection.commit()

# loadObj = LoadData()
# confObj =config()
# df_config = confObj.readConfig()
# database = confObj.getDatabase(df_config)

# loadObj.createEmployeeTable(database)
# loadObj.createEmployeeDetailsTable(database)
# loadObj.createPayrollTable(database)
# loadObj.createAgencyTable(database)
# loadObj.writeTable(database,agency,employee,employee_details,payroll_reference)