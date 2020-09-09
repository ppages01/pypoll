import csv
import sys

import numpy as np

with open("election_data.csv") as csv_file:
    csv_reader = csv.DictReader(csv_file)

    rows = list(csv_reader)
    votes = 0
    candidates = []
    count = 0
    old_tally = 0

    for row in rows:
        votes += 1
        candidates.append(row['Candidate'])
    # use numpy to get unique list candidates
    x = np.array(candidates)
    x_name = np.unique(x)
    # result table
    print("Election Results")
    print("-" * 25)
    print(f'Total Votes: {votes}')
    print("-" * 25)
    # loop through candidates(unique names,x_name), count their votes off list,
    # perform calc(s) and determine winner
    for name in x_name:
        name = x_name[count]
        tally = candidates.count(x_name[count])
        pct = round((tally / votes) * 100, 2)
        print(f'{name}: {pct} ({tally})')
        if tally > old_tally:
            winner = name
        old_tally = tally
        count += 1
    print("-" * 25)
    print(f'Winner:{winner}')
    print("-" * 25)
