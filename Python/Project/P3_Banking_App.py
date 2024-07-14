class Bank:
    def __init__(self, initial_amount=0.00):
        self.balance = initial_amount

    def log_transaction(self, transaction_string):
        with open("transactions.txt","a") as file:
            file.write(f"{transaction_string} \t\t\t Balance: {self.balance}\n")

    def withdrawal(self, amount):
        try:
            amount = float(amount)
        except ValueError:
            amount = 0
        if amount:
            self.balance = self.balance - amount
            self.log_transaction(f"withdrew {amount}")

    def deposit(self, amount):
        try:
            amount = float(amount)
        except ValueError:
            amount = 0
        if amount:
            self.balance = self.balance + amount
            self.log_transaction(f"deposited {amount}")

account = Bank(50.50)
while True:
    try:
        action = input("what kind of action do you want to take? ")
    except KeyboardInterrupt:
        print("\nleaving the ATM\n")
        break
    if action in ["withdrawal", "deposit"]:
        if action == "withdrawal":
            amount = input("how much do you want to take out? ")
            account.withdrawal(amount)
        else:
            amount = input("how much do you want to put in? ")
            account.deposit(amount)
        print("your balance is", account.balance)
    else:
        print("that is not a valid action. try again.")