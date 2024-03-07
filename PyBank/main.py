import os
import csv

from pathlib import Path 

datafile= os.path.join("Resources","budget_data.csv")

date = []
total_profit = []
monthly_profit_change = []

with open(datafile, newline="", encoding="utf-8") as budget:
    csvreader=csv.reader(budget, delimiter=",")
    header=next(csvreader)

    for row in csvreader:
        date.append(row[0])
        total_profit.append(int(row[1]))

    for i in range(len(total_profit)-1):

        monthly_profit_change.append(total_profit[i+1]-total_profit[i])

max_increase= max(monthly_profit_change)
max_decrease= min(monthly_profit_change)

max_increase_month = monthly_profit_change.index(max(monthly_profit_change))+1
max_decrease_month = monthly_profit_change.index(min(monthly_profit_change))+1

#Print Analysis

print("Financial Analysis")
print("-----------------------------")
print(f"Total Months: {len(date)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
print(f"Greatest Increase in Profits: {date[max_increase_month]} (${(str(max_increase))})")
print(f"Greatest Decrease in Profits: {date[max_decrease_month]} (${(str(max_decrease))})")

#Output .txt file

output_file= os.path.join('Analysis', 'Financial_Analysis_Summary.txt')

with open(output_file, "w") as file:
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(date)}")
    file.write("\n")
    file.write(f"Total: ${sum(total_profit)}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {date[max_increase_month]} (${(str(max_increase))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {date[max_decrease_month]} (${(str(max_decrease))})")


