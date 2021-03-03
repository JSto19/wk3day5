class ROI:
    def __init__(self):
        self.total_inv = 0

class Income:
    def __init__(self):
        self.rent = float(input("Monthly rent per unit(Numbers only without dots please): "))
        self.laundry = float(input("Laundry units charge times # of washer/dryer units(Numbers only without dots please): "))
        self.storage = float(input("Monthly charge added to rent for storage unit(s)(Numbers only without dots please): "))
        self.misc = float(input("Misc expenses charged(Numbers only without dots please): "))
        self.total_income = self.rent + self.laundry + self.storage + self.misc
        print(self.total_income)

class Utilities:
    def __init__(self):
        self.electric = float(input("Electric minimum per month(Numbers only without dots please): "))
        self.water = float(input("Water minimum charge per month(Numbers only without dots please): "))
        self.sewer = float(input("Septic service charge per month(Numbers only without dots please): "))
        self.garbage = float(input("Garbage service charge per month(Numbers only without dots please): "))
        self.gas = float(input("Gas bill per month average(Numbers only without dots please): "))
        self.total_util = self.electric + self.water + self.sewer + self.garbage + self.gas
        print(self.total_util)

class Expense:
    def __init__(self):
        self.tax = float(input("Tax charged per month(Numbers only without dots please): "))
        self.utilities_object = Utilities()
        self.utilities = self.utilities_object.total_util
        self.insurance = float(input("Insurance billed per month(Numbers only without dots please): "))
        self.yans = float(input("Yard and snow maintenance per month(Numbers only without dots please): "))
        self.vacancy = float(input("Income witheld for vacancy per month(Numbers only without dots please): "))
        self.repairs = float(input("Income witheld for repairs per month(Numbers only without dots please): "))
        self.capex = float(input("Cap expense per month witheld(Numbers only without dots please): "))
        self.propertymanager = float(input("Property Manager costs per month(Numbers only without dots please): "))
        self.mortgage = float(input("Monthly mortgage payment per month(Numbers only without dots please): "))
        self.total_ex = self.tax + self.utilities + self.insurance + self.yans + self.vacancy + self.repairs + self.capex + self.propertymanager + self.mortgage
        print(self.total_ex)

class CashFlow:
    def __init__(self):
        self.cashflow_ex_object = Expense()
        self.renter_expense = self.cashflow_ex_object.total_ex
        self.cashflow_object = Income()
        self.rent_multiple = self.cashflow_object.total_income
        self.rent_units = float(input("#units with this property averaging half units rented(Numbers only without dots please): "))
        self.per_year = self.rent_units *.5 * 12 * (self.rent_multiple - self.renter_expense)

class Loan_InvApp:
    def __init__(self):
        self.down_pay = float(input("How much down payment (Numbers only without dots please): "))
        self.close_cost = float(input("How much closing costs (Numbers only without dots please): "))
        self.rehab = float(input("How much for rehab (Numbers only without dots please): "))
        self.misc = float(input("Any misc items (Numbers only without dots please): "))
        self.total_inv = self.down_pay + self.close_cost + self.rehab + self.misc
        print(self.total_inv)

class InvProp:
    def __init__(self):
        self.income = Income()
        self.expense = Expense()
        self.cashflow = CashFlow()
        self.loaninvapp = Loan_InvApp()

    def actualROI(self):
        self.cashflow.per_year
        self.loaninvapp.total_inv
        print('Your ROI on total investment is: {self.cashflow.per_year/self.loaninvapp.total_inv*100}%')
    
def run():
    InvProp()

run()