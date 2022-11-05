import sqlite3
import pandas as pd

try:
    sqliteConnection = sqlite3.connect(r"C:\sqlite\NYC_payroll_data.db")
    cursor = sqliteConnection.cursor()
    print("Database created and Successfully Connected to SQLite")

    sqlite_select_Query = "select sqlite_version();"
    cursor.execute(sqlite_select_Query)
    record = cursor.fetchall()
    print("SQLite Database Version is: ", record)
    cursor.close()

except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)
finally:
    if (sqliteConnection):
        sqliteConnection.close()
        print("The SQLite connection is closed")

try:
    sqliteConnection = sqlite3.connect(r'C:\sqlite\NYC_payroll_data.db')
    employee_create_table_query = '''CREATE TABLE IF NOT EXISTS employee (employee_id INT PRIMARY KEY,
                                 employee_name TEXT NOT NULL UNIQUE);'''

    cursor = sqliteConnection.cursor()
    print("Successfully Connected to SQLite")
    cursor.execute(employee_create_table_query)
    sqliteConnection.commit()
    print("SQLite table created")
    # --------------------------------------------------------------------------------------
    agency_create_table_query = '''CREATE TABLE IF NOT EXISTS agency (payroll_number INT PRIMARY KEY,
                                 agency_name TEXT NOT NULL UNIQUE);'''
    cursor = sqliteConnection.cursor()
    cursor.execute(agency_create_table_query)
    sqliteConnection.commit()
    print("SQLite table created")
    # --------------------------------------------------------------------------------------
    payroll_ref_create_table_query = '''CREATE TABLE IF NOT EXISTS payroll_reference (payroll_number INT,
                                 employee_id INT PRIMARY KEY);'''
    cursor = sqliteConnection.cursor()
    cursor.execute(payroll_ref_create_table_query)
    sqliteConnection.commit()
    print("SQLite table created")
    # --------------------------------------------------------------------------------------
    employee_details_create_table_query = '''CREATE TABLE IF NOT EXISTS employee_details (employee_id INT PRIMARY KEY,title_description TEXT,work_location_borough TEXT,fiscal_year INT,pay_basis TEXT,base_salary_USD REAL,work_hours REAL, gross_salary_USD REAL, overtime_hours REAL,overtime_commission_USD REAL, other_pay_USD REAL);'''
    cursor = sqliteConnection.cursor()
    cursor.execute(employee_details_create_table_query)
    sqliteConnection.commit()
    print("SQLite table created")
    cursor.close()

except sqlite3.Error as error:
    print("Error while creating a sqlite table", error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("sqlite connection is closed")

agency= 'C:/Users/mailp/soen/app/Tables/agency.csv'

df1 = pd.read_csv(agency,dtype='unicode',engine='python')

employee= 'C:/Users/mailp/soen/app/Tables/employee.csv'

df2 = pd.read_csv(employee,dtype='unicode',engine='python')

payroll_reference= 'C:/Users/mailp/soen/app/Tables/payroll.csv'

df3 = pd.read_csv(payroll_reference,dtype='unicode',engine='python')

employee_details= 'C:/Users/mailp/soen/app/Tables/employee_details.csv'

df4 = pd.read_csv(employee_details,dtype='unicode',engine='python')

sqliteConnection = sqlite3.connect(r'C:\sqlite\NYC_payroll_data.db')
cur = sqliteConnection.cursor()
# -------------------------------------------------------------------------------------
df1.to_sql('agency', sqliteConnection, if_exists='replace', index=False) # - writes the pd.df to SQLIte DB
pd.read_sql('select * from agency', sqliteConnection)
#--------------------------------------------------------------------------------------
df2.to_sql('employee', sqliteConnection, if_exists='replace', index=False) # - writes the pd.df to SQLIte DB
pd.read_sql('select * from employee', sqliteConnection)
#--------------------------------------------------------------------------------------
df3.to_sql('payroll_reference', sqliteConnection, if_exists='replace', index=False) # - writes the pd.df to SQLIte DB
pd.read_sql('select * from payroll_reference', sqliteConnection)
#--------------------------------------------------------------------------------------
df4.to_sql('employee_details', sqliteConnection, if_exists='replace', index=False) # - writes the pd.df to SQLIte DB
pd.read_sql('select * from employee_details', sqliteConnection)
#--------------------------------------------------------------------------------------

sqliteConnection.commit()
sqliteConnection.close()