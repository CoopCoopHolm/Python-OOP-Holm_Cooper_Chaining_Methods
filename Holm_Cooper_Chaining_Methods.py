class User:
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account_balance = 0
        
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")
        return self
    def transfer_money(self, other_user, amount):
        other_user.make_deposit(amount)
        self.make_withdrawal(amount)
        return self
coopcoopholm = User("Cooper Holm", "coop.coop@coop.com")
jodoe = User("Joe Doe", "joe@joe.com")
goobypls = User("Gooby Please", "gooby@please.com")

coopcoopholm.make_deposit(34869500).make_deposit(5982870).make_deposit(12078500).make_withdrawal(801980).display_user_balance()
        
jodoe.make_deposit(1593841).make_deposit(25483157).make_withdrawal(11687).make_withdrawal(332520).display_user_balance()


goobypls.make_deposit(20).make_withdrawal(5).make_withdrawal(5).make_withdrawal(5).display_user_balance()


coopcoopholm.transfer_money(goobypls,3)
coopcoopholm.display_user_balance()
goobypls.display_user_balance()
