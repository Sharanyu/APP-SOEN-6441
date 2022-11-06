import pandas as pd
from sodapy import Socrata
import time
import sqlite3

data_source= 'C:/Users/shara/Desktop/app/NYC_payroll_data_cleaned_indexed.csv'

df = pd.read_csv(data_source,dtype='unicode',engine='python')

agency = df[['payroll_number','agency_name']]
employee = df[['employee_id','employee_name']]
payroll_reference = df[['payroll_number','employee_id']]
employee_details = df[['employee_id','title_description','work_location_borough','fiscal_year','pay_basis','base_salary_USD','work_hours', 'gross_salary_USD', 'overtime_hours','overtime_commission_USD', 'other_pay_USD']]
agency = agency.drop_duplicates()
employee_details = employee_details.drop_duplicates()
employee = employee.drop_duplicates()
payroll_reference =payroll_reference.drop_duplicates()

agency.to_csv('C:/Users/shara/Desktop/app/Tables/agency.csv',index=False)
employee_details.to_csv('C:/Users/shara/Desktop/app/Tables/employee_details.csv',index=False)
employee.to_csv('C:/Users/shara/Desktop/app/Tables/employee.csv',index=False)
payroll_reference.to_csv('C:/Users/shara/Desktop/app/Tables/payroll.csv',index=False)