# importing necessary objects for testing the methods
from models import modelObj

# Positive scenario - function to test the method find_emp with employee_id '1234' in the database and check if it is "YOLANDA M CASTILLO-CARDEN"
def test_find_emp1():
    assert modelObj.find_emp("1234")[0]["employee_name"] == "YOLANDA M CASTILLO-CARDEN"


# Negative scenario - function to test the method find_emp with employee_id '15877' in the database and check if it is "some Firstname and some Lastname"
def test_find_emp2():
    assert (
        modelObj.find_emp("15877")[0]["employee_name"]
        == "some Firstname and some Lastname"
    )


# Positive scenario - function to test the method find_emp with employee_id '5212' in the database and check his/her title is "CHILD PROTECTIVE SPECIALIST"
def test_find_emp3():
    assert (
        modelObj.find_emp("5212")[0]["title_description"]
        == "CHILD PROTECTIVE SPECIALIST"
    )


# Positive scenario - function to test the method view_emp in the database and check if it returns only 5 records as expected.
def test_view_emp():
    data = modelObj.view_emp()[0]
    assert len(data) == 5


# Positive scenario - function to test the method view_emp_from with location as 'BRONX' in the database and check if any records are found.
def test_view_emp_from_bronx():
    data = modelObj.view_emp_from("BRONX")
    assert len(data) > 0


# Positive scenario - function to test the method view_emp_from with location as 'MANHATTAN' in the database and check if any records are found.


def test_view_emp_from_manhattan():
    data = modelObj.view_emp_from("MANHATTAN")
    assert len(data) > 0


# Positive scenario - function to test the method view_emp_from with location as 'QUEENS' in the database and check if any records are found.


def test_view_emp_from_queens():
    data = modelObj.view_emp_from("QUEENS")
    assert len(data) > 0


# Positive scenario - function to test the method view_emp_from with location as 'RICHMOND' in the database and check if any records are found.


def test_view_emp_from_richmond():
    data = modelObj.view_emp_from("RICHMOND")
    assert len(data) > 0


# Positive scenario - function to test the method view_emp_from with location as 'BROOKLYN' in the database and check if any records are found.


def test_view_emp_from_brooklyn():
    data = modelObj.view_emp_from("BROOKLYN")
    assert len(data) > 0


# Negative scenario - function to test the method view_emp_from with location as 'MONTREAL' in the database and check if any records are found. Ofcourse it will not pass as Montreal is not located in New York.


def test_view_emp_from_montreal():
    data = modelObj.view_emp_from("MONTREAL")
    assert len(data) > 0
