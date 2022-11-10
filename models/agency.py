class agency:
    def __init__(self):
        self.payroll_number=None
        self.agency_name=None
    def set_payroll_number(self,pno):
        self.payroll_number=pno
        
    def set_agency_name(self,Aname):
        self.agency_name=Aname

    def get_payroll_number(self):
        return self.payroll_number

    def get_agency_name(self):
        return self.agency_name

agency = agency()