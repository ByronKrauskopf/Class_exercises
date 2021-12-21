# Modules
import os
import csv

# Prompt user for video lookup
video = input("What show or movie are you looking for? ")

# Set path for file
csvpath = os.path.join("..",'Resources', 'netflix_ratings.csv')
print(csvpath)
# Open the CSV
with open(csvpath) as csvfile:

    # Loop through looking for the video
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvfile)
