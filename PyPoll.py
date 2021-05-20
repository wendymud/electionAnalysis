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

# Open the election results and read the file.
with open(file_to_load) as election_data:

# Read and analyze the data here.
    file_reader = csv.reader(election_data)

# Print each row in the CSV file.
#    for row in file_reader:
#       print(row)

#Print the header row.
    headers = next(file_reader)
    print(headers)


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