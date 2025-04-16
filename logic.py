from errorr import DepositError, WithdrawError, InsufficientAmountError

accounts = {
    "12345": {"pin": "1234", "balance": 5000, "transaction_history": []},
    "67890": {"pin": "5678", "balance": 3000, "transaction_history": []}
}


def dep(acnumber):
    amt = float(input("Enter the amount to deposit: "))
    if amt <= 0:
        raise DepositError
    else:
        accounts[acnumber]["balance"] += amt
        transaction(acnumber, "Deposit", amt)
        print(f"You have deposited: {amt}rs. New Balance: {accounts[acnumber]['balance']}rs.")


def withdraw(acnumber):
    amt = float(input("Enter the amount to withdraw: "))
    if amt <= 0:
        raise WithdrawError
    elif accounts[acnumber]["balance"] < amt:
        raise InsufficientAmountError
    else:
        accounts[acnumber]["balance"] -= amt
        transaction(acnumber, "Withdraw", amt)
        print(f"You have withdrawn: {amt}rs. Current Balance: {accounts[acnumber]['balance']}rs.")


def balance(acnumber):
    print(f"Your current balance: {accounts[acnumber]['balance']}rs.")


def transaction(acnumber, action, amount):
    from datetime import datetime
    transaction_history = accounts[acnumber]["transaction_history"]
    balance = accounts[acnumber]["balance"]
    transaction_history.append({
        "action": action,
        "amount": amount,
        "balance": balance,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })


def mini_statement(acnumber):
    print("\nMini Statement:")
    print("{:<20} {:<10} {:<10} {:<10}".format("Timestamp", "Action", "Amount", "Balance"))
    print("-" * 60)
    for transaction in accounts[acnumber]["transaction_history"][-5:]:
        print("{:<20} {:<10} {:<10} {:<10}".format(
            transaction["timestamp"],
            transaction["action"],
            transaction["amount"],
            transaction["balance"]
        ))
    print("-" * 60)


def authenticate(acnumber):
    attempts = 3
    while attempts > 0:
        entered_pin = input("Enter your PIN: ")
        if entered_pin == accounts[acnumber]["pin"]:
            return True
        else:
            attempts -= 1
            print(f"Incorrect PIN. {attempts} attempts left.")
    print("Too many incorrect attempts. Exiting...")
    return False

