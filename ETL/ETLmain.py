from configClass import config
from datapull import Extract
from datacleaning import Transform
from indexing import Index
from TableData import TableData
from push_data import LoadData

if __name__ == '__main__':
    extract = Extract()
    transform = Transform()
    indexObj = Index()
    tdObj = TableData()
    pdObj = LoadData()
    configObj = config()
    
    raw_data = extract.get_data()
    transformed_data = transform.transformdata(raw_data)
    indexed_data = indexObj.indexdata(transformed_data)
    agencyModel,employeeModel,payrollModel,employeedetailsModel = tdObj.split(indexed_data)
    pdObj.createEmployeeTable(configObj.getDatabase(configObj.readConfig()))
    pdObj.createEmployeeDetailsTable(configObj.getDatabase(configObj.readConfig()))
    pdObj.createPayrollTable(configObj.getDatabase(configObj.readConfig()))
    pdObj.createAgencyTable(configObj.getDatabase(configObj.readConfig()))
    pdObj.writeTable(configObj.getDatabase(configObj.readConfig()),agencyModel,employeeModel,payrollModel,employeedetailsModel)