import random
import time
from faker import Faker



def run_atm():
    # Correct indentation for function body
    fake = Faker('en_PK')

    account_holder = fake.name()
    account_number = random.randint(10000, 99999)
    balance = random.randint(1000, 50000)

    print("===========================")
    print("   WELCOME TO THE ATM      ")
    print("===========================")

    input()
    print("\nReading card... Please wait.")
    time.sleep(2)

    print("\n---------------------------")
    print(f"Welcome, {account_holder}!")
    print(f"Account Number: {account_number}")
    print("---------------------------")

    while True:
        print("\nPlease choose an option:")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Log Out")
        
        choice = input("\nEnter choice (1-4): ").strip()

        if choice == '1':
            print(f"\n[BALANCE] Your current balance is: ${balance:,.2f}")

        elif choice == '2':  # Fixed missing choice condition
            try:
                # Removed corrupted Chinese character line
                amount = float(input("\nEnter amount to deposit: $"))
                if amount > 0:  # Fixed 'e' typo to '0'
                    balance += amount
                    print(f"[SUCCESS] ${amount:,.2f} deposited successfully.") # Fixed 'successflily' typo
                    print(f"New Balance: ${balance:,.2f}")
                else:
                    print("[ERROR] Deposit amount must be greater than zero.")
            except ValueError:
                print("[ERROR] Invalid input. Please enter a valid number.")
                
        elif choice == '3':
            try:
                amount = float(input("\nEnter amount to withdraw: $"))

                if amount > balance:
                    # Fixed broken string and missing bracket
                    print(f"[ERROR] Insufficient funds! Your balance is ${balance:,.2f}")
                elif amount <= 0:  # Fixed 'θ' typo to '0' and completed line
                    print("[ERROR] Withdrawal amount must be greater than zero.")
                else:
                    balance -= amount
                    print(f"[SUCCESS] ${amount:,.2f} withdrawn successfully.") # Fixed unclosed quote
                    print(f"Remaining Balance: ${balance:,.2f}")
            except ValueError:
                print("[ERROR] Invalid input. Please enter a valid number.")

        elif choice == '4':
            # Fixed unclosed string literal
            print(f"\nThank you for using our ATM, {account_holder}. Goodbye!")
            break
        else:
            print("[ERROR] Invalid selection. Please choose a number from 1 to 4.")

# Run the application
run_atm()

