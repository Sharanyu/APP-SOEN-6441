import pandas as pd

class config:
    def __init__(self):
        pass
    def readConfig(self):
        return pd.read_csv("configs.csv",quotechar="'")
    def getStaging(self,configdf):
        return configdf.query('operation == "Datapull" & configname == "staginglocation"').value.values.tolist()[0]
    def getDataURL(self,configdf):
        return configdf.query('operation == "Datapull" & configname == "data_url"').value.values.tolist()[0]
    def getDataset(self,configdf):
        return configdf.query('operation == "Datapull" & configname == "data_set"').value.values.tolist()[0]
    def getDatabase(self,configdf):
        return configdf.query('operation == "Datapull" & configname == "database"').value.values.tolist()[0]
    def getToken(self,configdf):
        return configdf.query('operation == "Datapull" & configname == "app_token"').value.values.tolist()[0]
    def getEmployeeTableName(self,configdf):
        return configdf.query('operation == "Pushdata" & configname == "tableemployee"').value.values.tolist()[0]
    def getPayrollTableName(self,configdf):
        return configdf.query('operation == "Pushdata" & configname == "tablepayroll"').value.values.tolist()[0]
    def getAgencyTableName(self,configdf):
        return configdf.query('operation == "Pushdata" & configname == "tableagency"').value.values.tolist()[0]
    def getEmployeeDetailsTableName(self,configdf):
        return configdf.query('operation == "Pushdata" & configname == "tableempdetails"').value.values.tolist()[0]