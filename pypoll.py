# The data we need to retreive:
# 1. Total number of votes cast
# 2. A complete list of candidates who received votes.
# 3. The percentage of votes each candidate won.
# 4. The total number of votes each candidate won.
# 5. The winner of the election based on popular vote.

import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources\election_results.csv")

# Create a filename variable to direct or indirect path to the file.
file_to_save = os.path.join("analysis\election_analysis.txt")

# 1. Initialize total vote counter.
total_votes = 0
candidate_options = []
candidate_votes = {}

# Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: Perform analysis.
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    # Print each row in the CSV file.
    
    # Print header row.
    headers = next(file_reader)
    
    # Print each row in CSV file
    for row in file_reader:
        total_votes += 1

        # 2. Complete list of candidates.
        # Print the candidate name from each row.
        candidate_name = row[2]

        # If candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            
            # Add candidate name to candidate list.
            candidate_options.append(candidate_name)

            # Begin tracking candidate vote count.
            candidate_votes[candidate_name] = 0

        # Count votes per candidate.
        candidate_votes[candidate_name] += 1

    # Using the with statement open the file as a text file
    with open(file_to_save, "w") as txt_file:
        elections_results = (
            f"\n Elections Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes}\n"
            f"-------------------------\n")
        print(elections_results, end="")
        txt_file.write(elections_results)       
        for candidate in candidate_votes:
            votes = candidate_votes[candidate]
             #3. Calculate percentage.
            vote_percentage = float(votes) / float(total_votes) * 100
            candidate_results = (
                f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
            # 4 Print candidate name and number of votes.
            print(candidate_results)
            txt_file.write(candidate_results)

    # Determine winning vote count and candidate.
    # Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            # Set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate

            winning_candidate_summary = (
                f"-------------------------\n"
                f"Winner: {winning_candidate}\n"
                f"Winning Vote Count: {winning_count:,}\n"
                f"Winning Percentage: {winning_percentage:.1f}%\n"
                f"-------------------------\n")
            print(winning_candidate_summary) 
            txt_file.write(winning_candidate_summary)
# Write some data to the file.
    #txt_file.write("Hello World.\n\nCounties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")