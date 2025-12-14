print("Welcome to SBI Bank")
acc_numbers = []
names = []
balances = []

while True:
    print("\n1. Create customer")
    print("2. View all customers")
    print("3. Check balance")
    print("4. Search customer by name")
    print("5. Withdraw amount")
    print("6. Delete account")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter name: ")
        acc_num = int(input("Enter account number: "))

        if acc_num in acc_numbers:
            print("Account already exists!")
        else:
            balance = float(input("Enter initial amount: "))
            acc_numbers.append(acc_num)
            names.append(name)
            balances.append(balance)
            print("Customer created successfully.")

    elif choice == 2:
        if acc_numbers:
            print("All Customers:")
            for i in range(len(acc_numbers)):
                print(f"Account Number: {acc_numbers[i]}, Name: {names[i]}, Balance: {balances[i]}")
        else:
            print("No customers found.")

    elif choice == 3:
        acc_num = int(input("Enter account number: "))
        if acc_num in acc_numbers:
            index = acc_numbers.index(acc_num)
            print("Balance:", balances[index])
        else:
            print("Account not found.")

    elif choice == 4:
        search_name = input("Enter customer name to search: ").lower()
        found = False
        for i in range(len(names)):
            if names[i].lower() == search_name:
                print(f"Account Number: {acc_numbers[i]}, Name: {names[i]}, Balance: {balances[i]}")
                found = True
        if not found:
            print("Customer not found.")

    elif choice == 5:
        acc_num = int(input("Enter account number: "))
        if acc_num in acc_numbers:
            index = acc_numbers.index(acc_num)
            withdraw = float(input("Enter amount to withdraw: "))
            if withdraw <= balances[index]:
                balances[index] -= withdraw
                print("Withdrawal successful. New balance:", balances[index])
            else:
                print("Insufficient balance.")
        else:
            print("Account not found.")

    elif choice == 6:
        acc_num = int(input("Enter account number: "))
        if acc_num in acc_numbers:
            index = acc_numbers.index(acc_num)
            acc_numbers.pop(index)
            names.pop(index)
            balances.pop(index)
            print("Customer deleted successfully.")
        else:
            print("Account not found.")

    elif choice == 7:
        print("Exiting program. Bye!")
        break

    else:
        print("Invalid choice.")
