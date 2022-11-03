import pandas as pd
from sodapy import Socrata
import time
import sqlite3

data_source= 'C:/Users/shara/Desktop/app/NYC_payroll_data.csv'

df = pd.read_csv(data_source,dtype='unicode',engine='python')

df["employee_name"] = df["first_name"] +' '+ df["last_name"]

df.drop(columns=['first_name','last_name'],axis=1, inplace=True)

# Renaming Columns

df.rename(columns={'leave_status_as_of_july_31': 'work_status','regular_hours': 'work_hours', 'base_salary':'base_salary_USD','regular_gross_paid':'gross_salary_USD','ot_hours':'overtime_hours','total_ot_paid':'overtime_commission_USD','total_other_pay':'other_pay_USD'}
,inplace=True, errors='raise')

# Remove unwanted columns

df.drop(columns='mid_init', inplace=True)

# status meaning not clear need to modify

df["work_status"].replace({"CEASED": "TERMINATED","SEASONAL" : "CONTRACTUAL"}, inplace=True)

# formatting date

df['agency_start_date'] = df['agency_start_date'].str.split('T').str[0]

df = df[['fiscal_year','payroll_number', 'agency_name', 'agency_start_date',
       'work_location_borough','employee_name', 'title_description', 'work_status',
       'base_salary_USD', 'pay_basis', 'work_hours', 'gross_salary_USD',
       'overtime_hours', 'overtime_commission_USD', 'other_pay_USD']]



duplicate_rows = df[df.duplicated(keep=False)]
df = df.drop_duplicates()
print("No. of rows after removing duplicates :",len(df))

df.dropna(subset = ['employee_name'],inplace=True)
df['employee_name'].astype('str').str.replace(r".", r"", regex=False)
df['employee_name'].astype('str').str.replace(r"-", r"", regex=False)

df.sort_values(['fiscal_year', 'employee_name'], ascending=[True, True], inplace=True)
df['work_location_borough'] = df.groupby(['agency_name'])['work_location_borough'].bfill()
df
df.drop(df.loc[df['employee_name']=='xxx xxx'].index, inplace=True)
df.drop(df.loc[df['pay_basis']=='Prorated Annual'].index, inplace=True)

df.to_csv('C:/Users/shara/Desktop/app/NYC_payroll_data_cleaned.csv')





