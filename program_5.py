# Program #5: Bank Balance
# Write a program that asks the user to enter the amount that he or she has budgeted for a month.
# A loop should then prompt the user to enter each of his or her expenses for the
# month and keep a running total. (Enter 0 to exit the loop)
# When the loop finishes, the program should display the amount that the
# user is over or under budget.

def main():
    budget = float(input("What is the budget for this month?: "))
    total_expenses = 0.0
    while True:
        expense = float(input("Enter an expense (or 0 to stop): "))
        if expense == 0:
            break
        total_expenses += expense
    difference = budget - total_expenses

    # Print whether the user is over or under budget
    if difference > 0:
        print(f"You are under budget by ${difference:.2f}")
    elif difference < 0:
        print(f"You are over budget by ${-difference:.2f}")
    else:
        print("You have exactly met your budget!")


if __name__ == '__main__':
    main()
