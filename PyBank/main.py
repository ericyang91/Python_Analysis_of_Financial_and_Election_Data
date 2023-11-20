# Import modules
import os
import csv
from path import path

# Define a function to calculate average
def average(list):
    return sum(list)/len(list)

def initial():
    read_path = os.path.join(path, "Resources", "budget_data.csv") # Uses the OS module to define reading path
    write_path = os.path.join(path, "Analysis", "financial_analysis.txt")

    with open(read_path, "r") as read_content: # with function ensures the file closes after use
        read_reader = csv.reader(read_content, delimiter = ",")
        months = []
        profit_losses = []
        net_pl_change = []
        datelist = []
        header = next(read_reader) # Skip the header
        first_row = next(read_reader) # Skip the first row and assign first row to a variable

        previous_net = int(first_row[1]) # First row variables are stored
        months.append(first_row[0])
        profit_losses.append(int(first_row[1]))

        for row in read_reader: # Iterate over the CSV rows
            months.append(row[0])
            profit_losses.append(int(row[1]))
            net_change = int(row[1]) - previous_net
            net_pl_change.append(net_change)
            previous_net = int(row[1]) # Re-assigns the previous_net
            datelist.append(row[0])

    total_number_of_months = len(months)
    net_total_profit_losses = sum(profit_losses)
    average_PL_change = average(net_pl_change)

    roster = dict(zip(net_pl_change, datelist)) # Create a zip object and turn that zip object into a dictionary
    greatest_increase = max(net_pl_change)
    greatest_increase_date = roster[(max(net_pl_change))] # Use dictionary to find the value corresponding to the key "max(net_pl_change)"
    greatest_decrease = min(net_pl_change)
    greatest_decrease_date = roster[(min(net_pl_change))]

    with open(write_path, "w") as write_content:
        write_content.write('Financial Analysis\n')
        write_content.write(f'The total number of months: {total_number_of_months}\n')
        write_content.write(f'The net total amount of "Profit/Losses" over the entire period: {net_total_profit_losses}\n')
        write_content.write(f'The average of changes in "Profit/Losses": {round(average_PL_change, 2)}\n')
        write_content.write(f'The greatest increase in profits was from {greatest_increase_date} in the amount of ${greatest_increase}.\n')
        write_content.write(f'The greatest decrease in profits was from {greatest_decrease_date} in the amount of ${greatest_decrease}.')

if __name__ == '__main__':
    initial()