# ---- ATM Machine Simulation

PIN = "1234" # Fixed PIN
balance = 1000  # Initial balance

# ATM Login
def main():
    pin = input("Enter ATM PIN: ")
    if pin == PIN:
        print("PIN Verified. Access Granted!\n")
        atm_menu()
    else:
        print("Incorrect PIN. Access Denied.")


# ATM Menu
def atm_menu():
    global balance
    while True:
        print("\n===== ATM Menu =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            print(f"Current Balance: {balance}\n")
        elif choice == "2":
            amount = float(input("Enter amount to deposit: "))
            balance += amount
            print(f"Deposited {amount}. New Balance = {balance}\n")
        elif choice == "3":
            amount = float(input("Enter amount to withdraw: "))
            if amount <= balance:
                balance -= amount
                print(f"Withdrawn {amount}. New Balance = {balance}\n")
            else:
                print("Insufficient balance.\n")
        elif choice == "4":
            print("Thank you for using ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()
