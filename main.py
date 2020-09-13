import csv
import sys
import numpy as np

with open("election_data.csv") as csv_file:
    csv_reader = csv.DictReader(csv_file)

    rows = list(csv_reader)
    votes = 0
    candidates = []

    for row in rows:
        votes += 1
        candidates.append(row['Candidate'])
    # use numpy to get unique list candidates
    x = np.array(candidates)
    x_name = np.unique(x)

    old_tally = 0
    count = 0
    results = {}
    for name in x_name:
        name = x_name[count]
        tally = candidates.count(x_name[count])
        # pct = round((tally / votes) * 100, 2)

        results[name] = tally
        if tally > old_tally:
            winner = name
        old_tally = tally
        count += 1
csv_file.close()

# result table
with open('results.txt', 'w') as f:
    sys.stdout = f
    print("Election Results")
    print("-" * 25)
    print(f'Total Votes: {votes}')
    print("-" * 25)
    for (k, v) in results.items():
        pct = round(v / votes * 100, 2)
        print(f'{k}: {pct}%  {v}')

    print("-" * 25)
    print(f'Winner:{winner}')
    print("-" * 25)
    f.close()
    sys.stdout = sys.__stdout__

with open('results.txt', 'r') as file:
    print(file.read())
