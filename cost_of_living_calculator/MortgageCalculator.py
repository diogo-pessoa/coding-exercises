class MortgageCalculator:
    """
    A class to calculate mortgage cost. For now just static values.
    Later we can calculate payments over n years and calculate the monthly interest
    charges and reduce to total debt to understand the compound interest effect.
    """

    def __init__(self, house_price, mortgage_period_months=360, mortgage_interest=2.5,
                 down_payment_percentage=0.10):
        self.down_payment = house_price * down_payment_percentage
        self.mortgage_period_months = mortgage_period_months
        self.mortgage_interest = mortgage_interest  # 2.6% annual interest rate (fixed)
        self.house_price = house_price
        self.mortgage_interest = self.mortgage_interest
        self.loan_amount = house_price - self.down_payment
        self.mortgage_monthly = self.get_monthly_payment()

    def get_monthly_payment(self):
        """
        Calculate the monthly mortgage payment.
        :return: Monthly mortgage payment.
        """
        monthly_rate = self.get_monthly_rate_percentage()
        P = self.loan_amount
        n = self.mortgage_period_months

        # Calculate monthly payment using the annuity formula
        monthly_payment = (P * monthly_rate) / (1 - (1 + monthly_rate) ** -n)

        return round(monthly_payment)

    def get_total_lent(self):
        """
        Calculate the total mortgage value (principal + interest).
        :return: Total amount lent over the mortgage period.
        """
        monthly_payment = self.get_monthly_payment()
        total_payment = monthly_payment * self.mortgage_period_months
        return total_payment

    def get_total_interest(self):
        """
        Calculate the total interest paid over the mortgage period.
        :return: Total interest paid.
        """
        monthly_payment = self.get_monthly_payment()
        total_payment = monthly_payment * self.mortgage_period_months
        total_interest = total_payment - self.loan_amount

        return round(total_interest)

    def get_total_repayable(self):
        """
        Calculate the total amount repayable over the mortgage period.
        :return: Total amount repayable.
        """
        total_interest = self.get_total_interest()
        total_repayable = self.loan_amount + total_interest

        return round(total_repayable)

    def get_monthly_rate_percentage(self):
        """
        # Convert annual rate to monthly and to decimal
        :return:
        """
        return self.mortgage_interest / 12 / 100

    def get_monthly_rate_charge(self):
        """
        Calculate the monthly interest rate.
        :return: Monthly interest rate.
        """
        return round(self.get_monthly_rate_percentage() * self.loan_amount)

    def get_interest_rate_cost_monthly(self):
        """
        Calculate the interest rate cost monthly. Based on statements roughly half of
        monthly repayment is interest. (interest is charged monthly on the remaining
        debt). For each month 1
        :return: Interest rate cost monthly.
        """
        return round(self.get_monthly_payment() - self.get_monthly_rate_charge())
