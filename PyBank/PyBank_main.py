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

 
# Export results as csv file.
# Specify the file to write to
output_path = os.path.join("..", "Homework3", "Financial_Analysis.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row
    csvwriter.writerow(['Total Months:', month_count])

    #Write the second row
    csvwriter.writerow(['Total:', '${:.0f}'.format(total)])

    # Write the third row
    csvwriter.writerow(['Average Change:', '${:.0f}'.format((total_change)/(month_count-1))])

    #Write the fourth row
    csvwriter.writerow(['Greatest Increase in Profit:', greatest_incr_mo, '${:.2f}'.format(greatest_increase)])

    # Write the fifth row
    csvwriter.writerow(['Greatest Decrease in Profit:', greatest_decr_mo, '${:.2f}'.format(greatest_decrease)])

   

