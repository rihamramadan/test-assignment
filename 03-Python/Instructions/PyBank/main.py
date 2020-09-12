import csv
import os

#csvpath = csvpath = os.path.join(".", "budget_data.csv")
csvpath = "budget_data.csv"

months_total = 0
profit_total = 0
net_change_list = [] 
greatest_increase = ["", 0]
greatest_decrease = ["", 999999999999]


with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    first_row = next(csvreader)
    months_total = months_total +1
    profit_total = profit_total + int(first_row[1])
    prev_net = int(first_row[1]) 

    for row in csvreader:
        profit_total = profit_total + int(row[1])
        months_total = months_total +1
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list = net_change_list + [net_change]
    
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change

    net_monthly_avg = sum(net_change_list) / len(net_change_list)

file_to_output = os.path.join("budget_analysis.txt")
output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {months_total}\n"
    f"Total: ${profit_total}\n"
    f"Average  Change: ${net_monthly_avg:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

# Print the output (to terminal)
print(output)

# Export the results to text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)