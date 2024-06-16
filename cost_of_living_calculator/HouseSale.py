class HouseSale:
    """
    when calculating the profit from the house sale (in the context of the of
    investment rates over the years. We also need to consider how much the monthly
    mortgage fee has paid of the debt. Normally about half of the monthly mortgage
    deducts from the debt, the other half is interest.

    """

    def __init__(self, sale_price, mortgage_debt, real_state_agent_commission,
                 solicitor_and_other_costs, monthly_mortgage,
                 total_investment_when_buying):
        self.sale_price = sale_price
        self.mortgage_debt = mortgage_debt
        self.real_state_agent_commission = real_state_agent_commission
        self.solicitor_and_other_costs = solicitor_and_other_costs
        self.monthly_mortgage = monthly_mortgage  # Will use to deduct bank interest
        self.total_investment_when_buying = total_investment_when_buying
        # from profit  # TODO - calculate how much of mortgage paid is lost in  #
        #  interest, calculate




    def __str__(self):
        return (f"Profit: {self.sale_price}\nmortgage debt: {self.mortgage_debt}\n"
                f"real state agent commission: "
                f"{self.real_state_agent_commission}\nsales costs: "
                f"{self.solicitor_and_other_costs}\nmonthly mortgage: "
                f"{self.monthly_mortgage}\ntotal investment when buying: "
                f"{self.total_investment_when_buying}")
