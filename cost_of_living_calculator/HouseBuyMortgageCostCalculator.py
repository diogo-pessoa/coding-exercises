import pandas as pd
from matplotlib import pyplot as plt

from cost_of_living_calculator.MortgageCalculator import MortgageCalculator


class HouseBuyMortgageCostCalculator:

    def __init__(self, house_price, mortgage_renegotiation_fee, house_buy_other_costs,
                 renovation_costs, admin_fees_per_year, number_of_years_repaid,
                 vlt_cost_per_year):
        self.mortgage_calc = MortgageCalculator(house_price)

        # Calculate the number of months paid
        self.months_repaid = number_of_years_repaid * 12

        self.mortgage_renegotiation_fee = mortgage_renegotiation_fee
        self.home_buy_other_costs = house_buy_other_costs
        self.renovation_costs = renovation_costs
        self.admin_fees_living_years = admin_fees_per_year * number_of_years_repaid
        self.vlt_cost_living_years = vlt_cost_per_year * number_of_years_repaid
        self.period_in_months = range(0, self.months_repaid)
        self.table_of_monthly_costs = pd.DataFrame(index=self.period_in_months,
                                                   columns=['mortgage', 'renovation',
                                                            'admin_fees', 'vlt',
                                                            'diluted_lump_sum',
                                                            'mortgage_renegotiation_fee',
                                                            'total'])
        # Load table with cost_per_month and totals
        self.load_table_cost_per_month()
        self.total_cost_per_month()

    def load_table_cost_per_month(self):
        for i in self.period_in_months:
            self.table_of_monthly_costs.loc[
                i, 'mortgage'] = self.mortgage_calc.get_monthly_payment()
            self.table_of_monthly_costs.loc[i, 'renovation'] = (
                    self.renovation_costs / self.months_repaid)
            self.table_of_monthly_costs.loc[
                i, 'vlt'] = self.vlt_cost / self.months_repaid
            self.table_of_monthly_costs.loc[
                i, 'admin_fees'] = self.admin_fees / self.months_repaid
            self.table_of_monthly_costs.loc[
                i, 'diluted_lump_sum'] = self.upfront_pay / self.months_repaid
            self.table_of_monthly_costs.loc[i, 'mortgage_renegotiation_fee'] = (
                    self.mortgage_renegotiation_fee / self.months_repaid)

    def total_cost_per_month(self):
        """
        spreading the down payment over the number of months and mortgage
        renegotiation fees.
        :return:
        """
        self.table_of_monthly_costs['total'] = (
                self.table_of_monthly_costs['mortgage'] + self.table_of_monthly_costs[
            'renovation'] + self.table_of_monthly_costs['vlt'] +
                self.table_of_monthly_costs['admin_fees'] + self.table_of_monthly_costs[
                    'diluted_lump_sum'] + self.table_of_monthly_costs[
                    'mortgage_renegotiation_fee'])

    def get_total_cost_per_year(self):
        """
        just an yearly view of the total cost
        :return:
        """
        return round(self.table_of_monthly_costs['total'][:12].sum())

    def get_total_cost(self):
        """
        Get the total cost of the mortgage
        :return:
        """
        return round(self.table_of_monthly_costs['total'].sum())

    def plot_total_cost_per_year_stacking(self):
        """
        Plot the total cost per year, stacked
        :return:
        """
        # Ensure 'year' column exists in the dataframe
        self.table_of_monthly_costs['year'] = (
                                                      self.table_of_monthly_costs.index // 12) + 1

        # Group by year and sum the costs
        yearly_costs = self.table_of_monthly_costs.groupby('year').sum()

        # Plot the stacked bar chart
        yearly_costs.plot(kind='bar', stacked=True)

        plt.title('Total Cost per Year (Stacked)')
        plt.xlabel('Year')
        plt.ylabel('Cost')
        plt.legend(title='Cost Categories')
        plt.show()

    def plot_mortgage_cost_per_month_five_years(self):
        """
        Plot the mortgage cost per month
        :return:
        """
        total_investment_over_60_months = self.table_of_monthly_costs['total'].sum()
        plt.figure(figsize=(10, 5))
        plt.plot(self.table_of_monthly_costs['total'].cumsum())
        # plt.axhline(total_investment_over_60_months, color='r', linestyle='--')
        plt.xlabel('Months')
        plt.ylabel('Cost')
        plt.legend(['Total cost', 'Total cost over 60 months'])
        plt.title('Total investment over 5 years')
        plt.show()

    def debt_left_after_years(self, paid_years=5):
        """
        Calculate the debt left after a certain number of years
        for the sake of simplicity I'll assume a fixed interest rate (and ignore
        inflation)
        :param paid_years: number of years paid
        :return:
        """
        monthly_fee = self.mortgage_monthly  # rate_per_annum = self.mortgage_interest
        # / 12 # 2.6% annual interest rate (fixed)
        mortgage_period_months = self.mortgage_period_months * 12  # 30 years

        total_debt = mortgage_period_months * monthly_fee

        debt = self.upfront_pay
        for i in range(paid_years * 12):
            debt = debt - self.table_of_monthly_costs.loc[i, 'mortgage']
        return debt

    def get_monthly_payment(self):
        """
        Calculate the monthly mortgage payment.
        :return: Monthly mortgage payment.
        """
        # Convert annual rate to monthly and to decimal
        monthly_rate = self.mortgage_interest / 12 / 100
        loan_amount = self.loan_amount
        repayment_period = self.mortgage_period_months

        # Calculate monthly payment using the annuity formula
        monthly_payment = (loan_amount * monthly_rate) / (
                1 - (1 + monthly_rate) ** -repayment_period)

        return monthly_payment

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

        return total_interest

    def get_total_repayable(self):
        """
        Calculate the total amount repayable over the mortgage period.
        :return: Total amount repayable.
        """
        total_interest = self.get_total_interest()
        total_repayable = self.loan_amount + total_interest

        return total_repayable

    def __str__(self):
        return self.table_of_monthly_costs.to_string()
