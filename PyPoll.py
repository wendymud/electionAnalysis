# Import the datetime class from the datetime module.
#import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
#now = dt.datetime.now()
# Print the present time.
#print("The current time is ", now)


import csv
import os

# Assign a variable for the file to load from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

#Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#1. Initialize a total vote counter
total_votes = 0

#creating a new candidate list
candidate_options = []

#declare an empty dictionary
candidate_votes = {}

# Determine winning vote count and candidate
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
# Read and analyze the data here.
    file_reader = csv.reader(election_data)
     #Read the header row.
    headers = next(file_reader) 
    # Print each row in the CSV file.
    for row in file_reader:
        #2 Add to the total vote count:
        total_votes += 1

        # Print candidate name from each row
        candidate_name = row[2]

        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            #2 Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1
#Save the results to our text file.
with open(file_to_save, "w") as txt_file:
        #After opening the file print the final vote count to the terminal.
        election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n")
        print(election_results, end="")
        #After printing the final vote cout to the terminal save the final vote count to the text file.
        txt_file.write(election_results)
        for candidate_name in candidate_votes:
            #retrieve vote count and percentage.
            votes = candidate_votes[candidate_name]
            vote_percentage = float(votes) / float(total_votes) * 100
            candidate_results = (
                f"{candidate_name}: {vote_percentage:.1f}% ({votes})\n")

            #Print each cnadidate's voter count and percentage to the terminal.
            print(candidate_results)
            #Save the candidate results to our text file.
            txt_file.write(candidate_results)

            #Determine the winning vote count, winning percentage, and winning candidate
            #Determine if the votes is greater than the winning count.
            if (votes > winning_count) and (vote_percentage > winning_percentage):
                #2 If true then set winning_count = votes and winning_percent = vote_percentage
                winning_count = votes
                #3 And set the winning_candidate equal to the candidate's name
                winning_candidate = candidate_name
                winning_percentage = vote_percentage

        # print out the winning candidate, vote count and percentage to terminal.

        winning_candidate_summary = (
            f"---------------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"----------------------------------\n")
        print(winning_candidate_summary)
            #Print each candidate, their voter count, and percentage to the terminal.
            #candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        #save the candidate results to our text file.
        txt_file.write(winning_candidate_summary)


#print(winning_candidate_summary)
# Create a filename variable to a direct or indirect path to the file.
#file_to_save = os.path.join("analysis", "election_analysis.txt")
    
    # Using the with statement open the file as a text file.
#with open(file_to_save, "w") as txt_file:

#Write some data to the file.
    #txt_file.write("Hello World")
    #txt_file.write("Counties in the Election\n")
    #txt_file.write("_________________________\n")
    # Write three counties to the file.
    #txt_file.write("Arapahoe\nDenver\nJefferson")

    # Close the file.
    #txt_file.close()