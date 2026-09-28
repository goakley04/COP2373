from functools import reduce
#First define the empty list of monthly expenses.
userExpenses = []

#Define the main function which will use lambda functions to analyze the user's monthly expenses list.
def main():
    while True:
        userExpenseType = input("Enter the type of monthly expense (or 'done' to exit): ")
#The user can type "done" when they are finished entering expenses.
        if userExpenseType.lower() == "done":
            break

        userExpenseCost = float(input("Enter the cost of this monthly expense: "))
#Append to the list using the user's input for expense type (string) and cost (float).
        userExpenses.append((userExpenseType, userExpenseCost))

#Define the functions to find the max and min in the list. The lambda function tells the max/min function
#to use the second value in each expense: expense cost.
    highest = max(userExpenses, key=lambda expense: expense[1])
    lowest = min(userExpenses, key=lambda expense: expense[1])

#Then print the result from max/min, and label the cost using the first value: expense type.
    print(f"Highest expense: {highest[0]} - ${highest[1]:.2f}")
    print(f"Lowest expense: {lowest[0]} - ${lowest[1]:.2f}")

#Finally define the function to total all expenses, which uses a current_total parameter and
#adds the cost of each expense to the total, starting at 0.0.
    totalExpenses = reduce(lambda current_total, expense: current_total + expense[1],
                           userExpenses, 0.0)
    print(f"Total monthly expenses: ${totalExpenses:.2f}")

if __name__ == "__main__":
    main()