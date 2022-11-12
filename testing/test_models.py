from models import modelObj, emp


def test_find_emp1():
    assert modelObj.find_emp("1234")[0]["employee_name"] == "YOLANDA M CASTILLO-CARDEN"


def test_find_emp2():
    assert (
        modelObj.find_emp("15877")[0]["employee_name"]
        == "some Firstname and some Lastname"
    )


def test_find_emp3():
    assert (
        modelObj.find_emp("5212")[0]["title_description"]
        == "CHILD PROTECTIVE SPECIALIST"
    )


def test_view_emp():
    data = modelObj.view_emp()[0]
    assert len(data) == 5


def test_view_emp_from_bronx():
    data = modelObj.view_emp_from("BRONX")
    assert len(data) > 0


def test_view_emp_from_manhattan():
    data = modelObj.view_emp_from("MANHATTAN")
    assert len(data) > 0


def test_view_emp_from_queens():
    data = modelObj.view_emp_from("QUEENS")
    assert len(data) > 0


def test_view_emp_from_richmond():
    data = modelObj.view_emp_from("RICHMOND")
    assert len(data) > 0


def test_view_emp_from_brooklyn():
    data = modelObj.view_emp_from("BROOKLYN")
    assert len(data) > 0


def test_view_emp_from_montreal():
    data = modelObj.view_emp_from("MONTREAL")
    assert len(data) > 0
