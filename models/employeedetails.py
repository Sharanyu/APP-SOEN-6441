class employeedetails:
    def _int_(self):
        self.employee_id =None,
        self.title_description=None,
        self.work_location_borough=None,
        self.fiscal_year=None, 
        self.pay_basis=None,
        self.base_salary_USD=None, 
        self.work_hours=None,
        self.gross_salary_USD=None, 
        self.overtime_hours=None, 
        self.overtime_commission_USD=None,
        self.other_pay_USD=None
    def set_location(self,location):
        self.work_location_borough = location
    def get_location(self):
        return self.work_location_borough
    
empdetails=employeedetails()