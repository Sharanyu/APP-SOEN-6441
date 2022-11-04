import pandas as pd
from sodapy import Socrata
import time
import sqlite3

data_source= 'C:/Users/shara/Desktop/app/NYC_payroll_data_cleaned.csv'

df = pd.read_csv(data_source,dtype='unicode',engine='python')

inputset = set(df['employee_name'].tolist())

output_dict = {val+1024:item for val,item in enumerate(inputset)}

df_emp = pd.DataFrame(output_dict.items(), columns=['employee_id', 'employee_name'])

final_df = df.merge(df_emp,on = 'employee_name')

final_df.drop(columns=df.columns[0], axis=1, inplace=True)

print(final_df.head())

first_col = final_df.pop('employee_id')
final_df.insert(0, 'employee_id',first_col)

final_df.to_csv('C:/Users/shara/Desktop/app/NYC_payroll_data_cleaned_indexed.csv',index=False)