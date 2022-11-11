class Employee:
    def __int__(self):
        self.employee_id = None
        self.employee_name = None

    def set_emp_id(self, id):
        self.employee_id = id

    def set_emp_name(self, name):
        self.employee_name = name

    def get_emp_id(self):
        return self.employee_id

    def get_emp_name(self):
        return self.employee_name


emp = Employee()
