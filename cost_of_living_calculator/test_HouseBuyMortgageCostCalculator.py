from unittest import TestCase

from cost_of_living_calculator.HouseBuyMortgageCostCalculator import HouseBuyMortgageCostCalculator


class TestMortgageCost(TestCase):
    def setUp(self):
        print(f"Running test: {self._testMethodName}")
        initial_cost = 7_000
        mortgage_renegotiation_fee = 3_600
        renovation_costs = 75_000
        admin_fees = 1100
        vlt_cost_per_year = 487
        number_of_years_paid = 5
        house_price = 365_000
        self.mortgage_cost = (
            HouseBuyMortgageCostCalculator(house_price, mortgage_renegotiation_fee, initial_cost,
                                           renovation_costs, admin_fees,
                                           number_of_years_paid, vlt_cost_per_year))

    def test_mortgage_value(self):
        self.assertEqual(365_000, self.mortgage_cost.house_price)

    def test_get_total_lent(self):
        self.assertEqual(365_000, self.mortgage_cost.get_total_lent())

    def test_get_monthly_payment(self):
        self.assertEqual(1_300, self.mortgage_cost.get_monthly_payment())
