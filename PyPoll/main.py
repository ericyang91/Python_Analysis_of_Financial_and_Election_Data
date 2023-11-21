# Import modules
import os
import csv
from file_path import path

# Define file paths for both reading and writing
read_path = os.path.join(path, "Resources", "election_data.csv")
write_path = os.path.join(path, "Analysis", "election_results.txt")

# Define the triggering function
def initial():
    with open(read_path, 'r') as read_store: # Read the CSV file
        read_reader = csv.reader(read_store, delimiter=",")
        header = next(read_reader) # Define header to skip it
        candidates = [] # For storing the unique candidate names
        counties = [] # For storing the unique county names
        
        for row in read_reader: # Iterate over the reader object
            if row[2] not in candidates:
                candidates.append(row[2]) # Add every unique candidate name
            if row[1] not in counties:
                counties.append(row[1]) # Add every unique county name

        build_dict(candidates, counties)

   
# Define a function that builds a Python dictionary
def build_dict(candidates, counties):
    with open(read_path, 'r') as read_store:
        read_reader = csv.reader(read_store, delimiter=",")
        header = next(read_reader)
        votes = [] # Stores all votes in candidate names
        dict = {county: {candidate: 0 for candidate in candidates} for county in counties} # Use nested dictionary comprehension
        for row in read_reader:
            votes.append(row[2])
            county = row[1]
            candidate = row[2]
            dict[county][candidate] += 1

        calculate_statistics(dict, votes, candidates)


def calculate_statistics(dict, votes, candidates):
    with open(write_path, "w") as write_store: # Prepare a writing object
        winning_candidate = max(candidates, key=lambda candidate: votes.count(candidate)) # Use the optional argument 'key' to use votes.count(candidate) as the value of interest
        for candidate in candidates:
            write_store.write(f"{candidate} received {votes.count(candidate)} votes in total.\n") # Finding the total vote each candidate received
        for county, candidate_votes in dict.items(): # The method dictionary.items() returns iterable key-value pairs. In this case, it iterates over the outer dictionary
            total_votes_by_county = sum(candidate_votes.values())
            write_store.write(f'\nCounty: {county}\n')
            write_store.write(f'Total number of votes in the county: {total_votes_by_county}\n')
            for candidate, votes in candidate_votes.items(): # Iterate over the inner dictionary
                percentage_of_vote = round(votes/total_votes_by_county*100, 2)
                write_store.write(f'Candidate name: {candidate}\n')
                write_store.write(f'Candidate number of votes: {votes}\n')
                write_store.write(f'Candidate vote in percentage: {percentage_of_vote}%\n\n')

        write_store.write(f"Congratulations to {winning_candidate} for winning this year's election!")

if __name__ == '__main__':
    initial()