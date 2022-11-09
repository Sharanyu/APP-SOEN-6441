import pandas as pd
from configClass import config


class Index:
    def __init__(self):
        self.configObj = config()
        self.configdf = self.configObj.readConfig()
        data_staging = self.configObj.getStaging(self.configdf)
    def indexdata(self,df):
        inputset = set(df['employee_name'].tolist())
    
        inputset2 = set(df['agency_name'].tolist())
    
        output_dict = {val+1024:item for val,item in enumerate(inputset)}
    
        output_dict2 = {val+100:item for val,item in enumerate(inputset2)}
    
        df_emp = pd.DataFrame(output_dict.items(), columns=['employee_id', 'employee_name'])
    
        df_agency = pd.DataFrame(output_dict2.items(), columns=['payroll_number', 'agency_name'])
    
        if df_agency.agency_name.nunique() == df_agency.payroll_number.nunique():
            df.drop(['payroll_number'], axis = 1, inplace = True)       
        final_df = df.merge(df_emp,on = 'employee_name')
        print(final_df.head())
        final_df = final_df.merge(df_agency,on = 'agency_name')
        print(final_df.head())
        
        first_col = final_df.pop('employee_id')
        final_df.insert(0, 'employee_id',first_col)
        print(final_df)
        second_col = final_df.pop('payroll_number')
        final_df.insert(1, 'payroll_number',second_col)
        
        return final_df