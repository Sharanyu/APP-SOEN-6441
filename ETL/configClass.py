import pandas as pd

class Config:
    def __init__(self):
        pass
    def read_config(self):
        return pd.read_csv("configs.csv",quotechar="'")
    def get_staging(self,configdf):
        return configdf.query('operation == "Datapull" & configname == "staginglocation"').value.values.tolist()[0]
    def get_data_url(self,configdf):
        return configdf.query('operation == "Datapull" & configname == "data_url"').value.values.tolist()[0]
    def get_dataset(self,configdf):
        return configdf.query('operation == "Datapull" & configname == "data_set"').value.values.tolist()[0]
    def get_database(self,configdf):
        return configdf.query('operation == "Datapull" & configname == "database"').value.values.tolist()[0]
    def get_token(self,configdf):
        return configdf.query('operation == "Datapull" & configname == "app_token"').value.values.tolist()[0]
    def get_employee_tableName(self,configdf):
        return configdf.query('operation == "Pushdata" & configname == "tableemployee"').value.values.tolist()[0]
    def get_payroll_tablename(self,configdf):
        return configdf.query('operation == "Pushdata" & configname == "tablepayroll"').value.values.tolist()[0]
    def get_agency_tableName(self,configdf):
        return configdf.query('operation == "Pushdata" & configname == "tableagency"').value.values.tolist()[0]
    def get_employee_details_tablename(self,configdf):
        return configdf.query('operation == "Pushdata" & configname == "tableempdetails"').value.values.tolist()[0]