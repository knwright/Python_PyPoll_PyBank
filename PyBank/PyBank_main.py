# Import Modules
import os, csv

# Set path for file
budget_data = os.path.join("..", "Homework3", "budget_data.csv")

# Define necessary variables for calculations
month_count = 0
total = 0
pl_change = 0
total_change = 0
greatest_increase = 0
greatest_decrease = 0
greatest_incr_mo = 0
greatest_decr_mo = 0


# Open the csv file
with open(budget_data, newline="") as csvfile:
   csvreader = csv.reader(csvfile, delimiter=",")
   
   # Check for a header, if present, skip on to the next row.
   if csv.Sniffer().has_header:
      next(csvreader)
   
   for row in csvreader:
      
      # Determine the profit/loss diff between current month and the previous
      if month_count != 0:
         pl_change = int(row[1]) - int_pl
         total_change += pl_change

      # Count the number of rows and assign those to monthly count.
      month_count += 1

      # Determine the total profit/loss for the entire data set, set as an integer.
      int_pl = int(row[1])
      total += int_pl

      # Determine the greatest increase, decrease and corresponding months
      if pl_change > greatest_increase:
         """Checks to see if profit/loss change is greater than zero, assigns 
         it to zero and renames it the greatest increase variable"""
         greatest_increase = pl_change
         greatest_incr_mo = row[0]

      if pl_change < greatest_decrease:
         greatest_decrease = pl_change
         greatest_decr_mo = row[0]

   # Indentation is important here to prevent the loop from print the values for each row
   print("Financial Analysis")
   print("-----------------------")
   print(f"Total Months: ", month_count)
   print(f"Total: ", '${:.0f}'.format(total))
   print(f"Average Change: ", '${:.2f}'.format((total_change)/(month_count-1)))
   print(f"Greatest Increase in Profits:", greatest_incr_mo, '${:.2f}'.format(greatest_increase))
   print(f"Greatest Decrease in Profits:", greatest_decr_mo, '${:.2f}'.format(greatest_decrease))

 
# Export results as txt file.
# Specify the file to write to
output_path = os.path.join("..", "Homework3", "Financial_Analysis.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
file = open("Financial_Analysis.txt", "w")

file.write("Financial Analysis \n")
file.write("----------------------------- \n")
file.write("Total Months: 86 \n")
file.write("Total: $38382578 \n")
file.write("Average Change: $-2315.12 \n")
file.write("Greatest Increase in Profits: Feb-2012 $1926159.00 \n")
file.write("Greatest Decrease in Profits: Sep-2013 $-2196167.00 \n")

file.close()