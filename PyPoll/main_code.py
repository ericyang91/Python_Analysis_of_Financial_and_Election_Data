# Read the CSV file
import os
import csv

read_path = os.path.join(r"C:\Users\ericj\OneDrive\Documents\Repositories\Python_Analysis_of_Financial_and_Election_Data\PyPoll", "Resources", "election_data.csv")

def initial():
    with open(read_path, 'r') as read_store:
        read_reader = csv.reader(read_store, delimiter=",")
        header = next(read_reader)
        total_votes = 0
        candidates = []
        counties = []
        for row in read_reader:
            if row[2] not in candidates:
                candidates.append(row[2])
            if row[1] not in counties:
                counties.append(row[1])
            total_votes += 1
        build_dict(candidates, counties)
    

def build_dict(candidates, counties):
    with open(read_path, 'r') as read_store:
        read_reader = csv.reader(read_store, delimiter=",")
        header = next(read_reader)
        dict = {county: {candidate: 0 for candidate in candidates} for county in counties}
        for row in read_reader:
            county = row[1]
            candidate = row[2]
            dict[county][candidate] += 1
        print(dict)
            

initial()


# number of votes each candidate received in total
# number of votes each candidate received in each county

# Winner, number of votes, percentage

# Interactive Pie chart, Bar chart, Table

# Write a report in a text format

