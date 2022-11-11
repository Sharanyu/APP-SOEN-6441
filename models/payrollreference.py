class PayrollReference:
    def _int_(self):
        self.payroll_number = None
        self.employee_id = None
    def set_emp_id(self,id):
        self.employee_id=id
        
    def set_payroll_number(self,pno):
        self.payroll_number=pno

    def get_emp_id(self):
        return self.employee_id

    def get_payroll_number(self):
        return self.payroll_number

payroll = PayrollReference()