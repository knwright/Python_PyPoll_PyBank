# Import Modules
import os, csv

# Set path for file
election_data = os.path.join("..", "Homework3", "election_data.csv")

# Define necessary variables for calculations
total_votes = 0
results = {}
candidates = []
cand_votetotal = []
vote_percent = []
winner_list = []

# Open the csv file
with open(election_data, newline="") as csvfile:
   csvreader = csv.reader(csvfile, delimiter=",")
  
   # Checks for header and skips it.
   if csv.Sniffer().has_header:
      next(csvreader)
   
   # Creates a dictionary of results from column 3 (Candidate) data
   # Counts the total number of votes cast
   # Counts the number of votes cast for each candidate and adds them
   for row in csvreader:

      total_votes += 1

      if row[2] in results.keys():
         results[row[2]] = results[row[2]] + 1
      
      else:
         results[row[2]] = 1

# Adds dictionary keys and values to candidates and candidate vote total
# lists respectively
for key, value in results.items():
   candidates.append(key)
   cand_votetotal.append(value)

# Creates vote percent list
for n in cand_votetotal:
   vote_percent.append('{:.3f}%'.format(round(n/total_votes*100, 2)))
  
# Zips candidates, number of votes and vote percentage into tuples
clean_data = list(zip(candidates, cand_votetotal, vote_percent))

# Creates winner
for candidates in clean_data:
    if max(cand_votetotal) == candidates[1]:
        winner_list.append(candidates)

# makes winner_list a str with the first entry
winner = winner_list[0]

# Export results as txt file.
# Specify the file to write to
output_file = os.path.join("..", "Homework3", "Election_Results.txt")

with open(output_file, 'w') as txtfile:
   txtfile.writelines('Election Results \n------------------------- \nTotal Votes: ' + str(total_votes) 
   + '\n-------------------------\n')
   for entry in clean_data:
      txtfile.writelines(entry[0] + ": " + str(entry[2]) + ' (' + str(entry[1]) + ')\n')
   txtfile.writelines('------------------------- \nWinner: ' + str(winner[0]) + '\n-------------------------')

# Prints file to terminal
with open(output_file, 'r') as readfile:
   print(readfile.read())

