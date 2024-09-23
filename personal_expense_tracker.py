total_spending = 0
expenses = ""
while True:
    print("\nMenu:")
    print("1. Add")
    print("2. View All")
    print("3. Total")
    print("4. Save")
   
    
    choice = input("Choose an option: ")

    if choice == '1':
        category = input("category: ")
        amount = int(input("amount: "))
        total_spending = total_spending + amount
        expenses = expenses + category + ": " + str(amount) + "\n"
        print("add", amount, "to", category)
        
    elif choice == '2':
        if expenses:
            print("expenses:")
            print(expenses)
        else:
            print("No expenses added.")
            
    elif choice == '3':
        print("total spending:", total_spending)
        
    elif choice == '4':
        with open("expenses.txt", "w") as result:
            print(expenses, file=result)
            print("total spending:",total_spending,file=result)
        print("saved to file.")
  
