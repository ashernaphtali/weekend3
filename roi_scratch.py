class rentalROI:

    def __init__(self):
        self.home_cost = 0
        self.downpayments = 0
        self.closing_costs = 0
        self.rehab = 0
        self.number_units = 0
        self.income_per_unit = 0
        self.taxes = 0
        self.insurance = 0
        self.utilities = 0
        self.hoa = 0
        self.lawncare = 0
        self.repairs = 0
        self.capex = 0
        self.prop_mgmt = 0
        self.mortgage = 0


# -----------------------INPUTS--------------------------------
    
    def details(self):
        print("Please enter the follwing information from your mortgage contract:")
        self.home_cost = int(input("Enter sale price for home: "))
        self.downpayments = int(input("Enter downpayment: "))
        self.closing_costs = int(input("Enter closing costs incurred: "))
        self.taxes = int(input("Enter monthly property taxes: "))
        self.insurance = int(input("Enter monthly homeowners insurance: "))
        self.number_units = int(input("Number of property's rental units: "))
        self.mortgage = int(input("Enter monthly mortgage payment: "))

        print("Please enter the follwing information from your property analysis: ")
        self.income_per_unit = int(input("Enter monthly income per unit: "))
        self.rehab = int(input("Enter estimated rehab costs: "))
        self.vacancy = int(input("Enter estimated vacancy costs allocated monthly: "))
        self.utilities = int(input("Enter monthly utilities cost: "))
        self.hoa = int(input("Enter monthly homeowners' association fees: "))
        self.lawncare = int(input("Enter monthly lawncare costs: "))
        self.repairs = int(input("Enter monthly estimated repairs costs: "))
        self.capex = int(input("Enter estimated capital expenditures allocated monthly: "))
        self.prop_mgmt = int(input("Enter monthly property management fees: "))
        self.total_investment = self.downpayments + self.closing_costs + self.rehab
        print(f"Your total investment is: {self.total_investment}")
        self.total_monthly_income = self.income_per_unit * self.number_units
        print(f"Your total monthly income is: {self.total_monthly_income}")
        self.total_monthly_expenses = self.taxes + self.insurance + self.mortgage + self.vacancy + self.utilities + self.hoa + self.lawncare + self.repairs + self.capex + self.prop_mgmt
        print(f"Your total monthly expenses are: {self.total_monthly_expenses}")
        self.cash_flows = self.total_monthly_income - self.total_monthly_expenses
        print(f"Your total monthly cash flows are: {self.cash_flows}")
        self.roi = (self.cash_flows*12) / self.total_investment
        self.roi_new = self.roi * 100
        print(f"Your estimated annual return on investment is: {self.roi_new}%")
        

# -----------------------INPUTS (END)--------------------------------


# ---------------------------CALLING IN (BEGINNING)-------------------------------
    def runAnalysis(self):
        while True:
            choice = input("Type 'begin' to start the rental property ROI analysis: ")
            if choice == "begin":
                self.details()

            elif choice == "quit":
                break

# ---------------------------CALLING IN (END)-------------------------------

rental_property_1 = rentalROI()
rental_property_2 = rentalROI()
rental_property_3 = rentalROI()

rental_property_1.details()