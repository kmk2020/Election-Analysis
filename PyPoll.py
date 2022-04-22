#Open the data file.

#Write down the names of all the candidates.

#Add a vote count for each candidate.

#Get the total votes for each candidate.

#Get the total votes cast for the election.

#import csv

#dir(csv)

# Open the election results and read the file.
import csv
import importlib
import os


file_to_load = 'Resources/election_results.csv'

# To do: perform analysis.
election_data = open(file_to_load, "r")

# Close the file.
election_data.close()

# Open the election results and read the file
with open(file_to_load) as election_data:

     # To do: perform analysis.
     print(election_data)

import os

print(dir(os))

print(dir(os.path))

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

     # Print the file object.
     #print(election_data) 
    
    # Read the file object with the reader function.
 file_reader = csv.reader(election_data)

 # Print the header row.
 headers = next(file_reader)
 print(headers)

#Print each row in the CSV file.
 #for row in file_reader: 
    #print(row[0]) 
 

     
