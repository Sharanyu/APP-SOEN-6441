from config_class import Config
from extract import Extract
from cleaner import Transform
from indexing import Index
from split_data import TableData
from loading import LoadData

if __name__ == '__main__':
    extract = Extract()
    transform = Transform()
    indexObj = Index()
    tdObj = TableData()
    pdObj = LoadData()
    configObj = Config()
    
    raw_data = extract.get_data()
    transformed_data = transform.transform_data(raw_data)
    indexed_data = indexObj.index_data(transformed_data)
    agencyModel,employeeModel,payrollModel,employeedetailsModel = tdObj.split(indexed_data)
    pdObj.create_employee_table(configObj.get_database(configObj.read_config()))
    pdObj.create_employee_details_table(configObj.get_database(configObj.read_config()))
    pdObj.create_payroll_table(configObj.get_database(configObj.read_config()))
    pdObj.create_agency_table(configObj.get_database(configObj.read_config()))
    pdObj.write_table(configObj.get_database(configObj.read_config()),agencyModel,employeeModel,payrollModel,employeedetailsModel)