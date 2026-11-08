class BankAcct:

    #Define the init method, ensure balance and interest are floats.
    def __init__(self, name, account, balance, interest):
        self.name = name
        self.account = account
        self.balance = float(balance)
        self.interest = float(interest)

    #Define the method for updating the interest rate.
    def interest_adjust(self, new_interest):
        self.interest = float(new_interest)
        print(f"Interest adjusted to {self.interest:}")

    #Define the method for withdraw/deposit.
    def balance_adjust(self, amount):
        self.balance += float(amount)
        if amount > 0:
            print(f"Deposited ${amount}\n")
        else:
            print(f"Withdrew ${amount}\n")

    def display_balance(self):
        print(f"Account balance: ${self.balance}\n")
        return self.balance

    #Calculate interest, based on user input for # of days.
    def calculate_interest(self, days):
        value = self.balance * self.interest * (days / 365)
        print(f"Estimated interest: ${value:.2f}\n")

    def __str__(self):
        return (f"Account Name: {self.name}\n"
                f"Account Number: {self.account}\n"
                f"Account Balance: ${self.balance}\n"
                f"Interest rate: {self.interest}\n")

def test_methods():
    test = BankAcct("Your Name", "0000012345", 50.00, 0.05)
    print(test)

    test.display_balance()

    test.balance_adjust(1000.00)

    test.display_balance()

    test.balance_adjust(-150)

    test.display_balance()

    days = int(input("Enter number of days for interest calculation: "))

    test.calculate_interest(days)

    test.interest_adjust(0.08)

    print(test)

if __name__ == "__main__":
    test_methods()
