from logic import dep, withdraw, balance, mini_statement, authenticate, accounts
from errorr import WithdrawError, DepositError, InsufficientAmountError
from menu import menu
def main():
    print("Verify Your Identity !")
    acnumber = None

    while acnumber is None:
        acnumber = input("Enter your account number: ")
        if acnumber not in accounts:
            print("Account not found. Please try again.")
            acnumber = None

    if authenticate(acnumber):
        while True:
            menu()
            try:
                choice = int(input("Enter your choice: "))
                match choice:
                    case 1:
                        try:
                            dep(acnumber)
                        except DepositError:
                            print("Error: Cannot deposit negative or zero amounts.")
                        except ValueError:
                            print("Error: Please enter a valid numeric amount.")
                    case 2:
                        try:
                            withdraw(acnumber)
                        except WithdrawError:
                            print("Error: Cannot withdraw negative or zero amounts.")
                        except ValueError:
                            print("Error: Please enter a valid numeric amount.")
                        except InsufficientAmountError:
                            print("Error: Insufficient funds in your account.")
                    case 3:
                        balance(acnumber)
                    case 4:
                        mini_statement(acnumber)
                    case 5:
                        print("Thank you for using the ATM. Bye!")
                        break
                    case _:
                        print("Invalid choice. Please select a valid option.")
            except ValueError:
                print("Error: Please enter a valid numeric choice.")

if __name__ == "__main__":
    main()

