# Program #3: Average Rainfall
# Write a program that uses nested loops to collect data and calculate the average
# rainfall over a period of years.
# The program should first ask for the number of years.
# The outer loop will iterate once for each year.
# The inner loop will iterate twelve times, once for each month.
# Each iteration of the inner loop will ask the user for inches of rainfall for each month.
# After all iterations, the program should display the number of months,
# the total inches of rainfall, and the average rainfall per month for the entire period.

def main():
    years = int(input("What is the number of years?: "))
    total_rainfall = 0
    total_months = years * 12

    for i in range(years):
        for month in range(12):
            rainfall = float(input(f"Enter rainfall for month {month + 1} of year {i + 1}: "))
            total_rainfall += rainfall

    average_rainfall = total_rainfall / total_months

    return total_months, total_rainfall, average_rainfall  # Returning all necessary values

if __name__ == '__main__':
    total_months, total_rainfall, average_rainfall = main()
    print(f"\n---Results---")
    print(f"Total Months: {total_months}")
    print(f"Total Rainfall Amounts: {total_rainfall}")
    print(f"Average Rainfall: {average_rainfall}")
