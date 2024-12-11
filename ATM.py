class ATM:
    def __init__(self):
        self.accounts = {
            2412: {"pin": 2412, "balance": 8000, "history": []},
            5678: {"pin": 5678, "balance": 5000, "history": []},
        }
        self.current_account = None

    def authentication(self):
        print("\n==== Welcome to the ATM ====")
        try:
            account_number = int(input("Enter your account number: "))
            pin = int(input("Enter your PIN: "))
            if (
                account_number in self.accounts
                and self.accounts[account_number]["pin"] == pin
            ):
                self.current_account = account_number
                print("\nLogin successful!")
                return True
            else:
                print("\nInvalid account number or PIN.")
                return False
        except ValueError:
            print("\nInvalid input! Please enter numbers only.")
            return False

    def check_balance(self):
        balance = self.accounts[self.current_account]["balance"]
        print(f"\nYour current balance is: ₹{balance}")

    def depositamount(self):
        try:
            amount = float(input("Enter the amount to deposit: ₹"))
            if amount <= 0:
                print("\nDeposit amount must be positive!")
            else:
                self.accounts[self.current_account]["balance"] += amount
                self.accounts[self.current_account]["history"].append(
                    f"Deposited ₹{amount}"
                )
                print(f"\n₹{amount} has been successfully deposited!")
        except ValueError:
            print("\nInvalid input! Please enter a valid amount.")

    def withdraw(self):
        try:
            amount = float(input("Enter the amount to withdraw: ₹"))
            if amount <= 0:
                print("\nWithdrawal amount must be positive!")
            elif amount > self.accounts[self.current_account]["balance"]:
                print("\nInsufficient balance!")
            else:
                self.accounts[self.current_account]["balance"] -= amount
                self.accounts[self.current_account]["history"].append(
                    f"Withdrew ₹{amount}"
                )
                print(f"\n₹{amount} has been successfully withdrawn!")
        except ValueError:
            print("\nInvalid input! Please enter a valid amount.")

    def show_transaction_history(self):
        history = self.accounts[self.current_account]["history"]
        if history:
            print("\n==== Transaction History ====")
            for record in history:
                print(record)
        else:
            print("\nNo transaction history available.")

    def logout(self):
        print("\nLogging out. Thank you for using the ATM!")
        self.current_account = None

    def main_menu(self):
        while True:
            print("\n==== ATM Main Menu ====")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. View Transaction History")
            print("5. Logout")

            try:
                choice = int(input("Choose an option (1-5): "))
                if choice == 1:
                    self.check_balance()
                elif choice == 2:
                    self.deposit()
                elif choice == 3:
                    self.withdraw()
                elif choice == 4:
                    self.show_transaction_history()
                elif choice == 5:
                    self.logout()
                    break
                else:
                    print("\nInvalid option! Please try again.")
            except ValueError:
                print("\nInvalid input! Please enter a number.")

if __name__ == "__main__":
    atm = ATM()
    while True:
        if atm.authentication():
            atm.main_menu()

