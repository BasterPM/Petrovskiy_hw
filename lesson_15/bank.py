class Bank:

    def __init__(self):
        self.money = 0

    def credit_funds(self, amount_of_money: int):
        self.money += amount_of_money

    def write_off_funds(self, amount_of_money: int):
        self.money -= amount_of_money

    def info(self):
        print(self.money)
