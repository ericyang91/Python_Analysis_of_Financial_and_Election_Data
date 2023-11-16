# Read the CSV file
import os
import csv
from file_path import path


read_path = os.path.join(path, "Resources", "election_data.csv")
write_path = os.path.join(path, "Analysis", "election_results.txt")


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
        calculate_statistics(dict)


def calculate_statistics(dict):
    with open(write_path, "w") as write_store:
        for county, candidate_votes in dict.items():
            total_votes_by_county = sum(candidate_votes.values())
            write_store.write(f'County: {county}\n')
            write_store.write(f'Total number of votes in the county: {total_votes_by_county}\n')
            for candidate, votes in candidate_votes.items():
                percentage_of_vote = round(votes/total_votes_by_county*100, 2)
                write_store.write(f'Candidate name: {candidate}\n')
                write_store.write(f'Candidate number of votes: {votes}\n')
                write_store.write(f'Candidate vote in percentage: {percentage_of_vote}%\n\n')


initial()