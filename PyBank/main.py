import os
import csv

csv_path = os.path.join("..", "PyBank", "Resources", "budget_data.csv")

total_months = []
total_profit = []
average_change = []
date = []
increase = []
decrease = []

with open(csv_path) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")

    header = next(csvreader)

    for row in csvreader:
        total_months.append(row[0])
        total_profit.append(int(row[1]))
        date.append(row [0])

    for x in range(1, len(total_profit)):
        average_change.append((int(total_profit[x]) - int(total_profit[x-1])))

    total_average_change = sum(average_change) / len(average_change)

    greatest_increase = max(average_change)

    greatest_decrease = min(average_change)

    greatest_date = date[average_change.index(max(average_change)) + 1]

    worst_date = date[average_change.index(min(average_change)) + 1]



print(f"Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: ${round(total_average_change,2)}")
print(f"Greatest Decrease in Profits: {greatest_date} (${max(average_change)})")
print(f"Greatest Decrease in Profits: {worst_date} (${min(average_change)})")


print(f"Financial Analysis", file=open("PyBank_analysis.txt", "a"))
print("----------------------------", file=open("PyBank_analysis.txt", "a"))
print(f"Total Months: {len(total_months)}", file=open("PyBank_analysis.txt", "a"))
print(f"Total: ${sum(total_profit)}", file=open("PyBank_analysis.txt", "a"))
print(f"Average Change: ${round(total_average_change,2)}", file=open("PyBank_analysis.txt", "a"))
print(f"Greatest Decrease in Profits: {greatest_date} (${max(average_change)})", file=open("PyBank_analysis.txt", "a"))
print(f"Greatest Decrease in Profits: {worst_date} (${min(average_change)})", file=open("PyBank_analysis.txt", "a"))