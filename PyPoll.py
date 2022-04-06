#The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter.
total_votes = 0

#Candidate Options
candidate_options = []

# Open the election results and read the file.
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read ans print te header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

    # If the candidate does not match any exisiting candidate...
    if candidate_name not in candidate_options:
        # Add the candidate name to the candidate list.
        candidate_options.append(candidate_name)

# Print the candidate list.
print(candidate_options)

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
open(file_to_save, "w")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Use the open statement to open the file as a text file.
outfile = open(file_to_save, "w")
# Write some data to the file.
outfile.write("Hello World")

# Close the file
outfile.close()

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:
    # Write three counties to the file.
    txt_file.write("Counties in the Election\n------------------------\nArapahoe\nDenver\nJefferson")
