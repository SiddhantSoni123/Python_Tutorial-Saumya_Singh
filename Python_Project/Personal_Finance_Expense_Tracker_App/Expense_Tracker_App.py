#Expense Tracker Project

expensesList = []   #List of Expenses in the form of Dictionary
print("Welcome to the Expense Tracker App: Let's check your expenses")

while True:
    print("<-----MENU----->")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Expenses")
    print("4. Exit")

    choice = int(input("Please Enter your choice: "))

#1.Add Expense
    if(choice == 1):
        date = input("Please Enter your date (YYYY-MM-DD): ")
        category = input("Please Enter your category: ")
        description = input("Please Enter your description: ")
        amount = float(input("Please Enter your amount: "))

        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        expensesList.append(expense)
        print("\nCool!! Your expense has been added successfully!")

#2.View All Expenses
    elif(choice == 2):
        if(len(expensesList) == 0):
            print("No expenses added! Go Get some expenditures done first!!")
        else:
            print("<-----This is the list of all your expenses!----->")
            count = 1
            for eachExpense in expensesList:
                print(f"Expense Number {count} -> {eachExpense['date']}, {eachExpense['category']}, {eachExpense['description']}, {eachExpense['amount']}")
                count = count + 1

#3.View Total Expenses
    elif(choice == 3):
        total = 0;
        for eachExpense in expensesList:
            total += eachExpense["amount"]

        print("\n Total Expenses: ", total)

#4.Exit
    elif(choice == 4):
        print("Thank You for using our App!!")
        break

    else:
        print("INVALID CHOICE! Please try again!")
