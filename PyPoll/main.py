import os
import csv

csv_path = os.path.join("..", "Pypoll", "Resources", "election_data.csv")

candidate = ""
can_votes = {}
total_votes = 0
percentage_of_candidate= {}
winner_total = 0
winner = ""

with open(csv_path) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    
    next(csvreader)
    
    for row in csvreader:
        
        total_votes = total_votes + 1
        
        candidate = row[2]
        
        if candidate in can_votes:
            can_votes[candidate] = can_votes[candidate] + 1
            
        else:
            can_votes[candidate] = 1   

for name, votes_ct in can_votes.items():
    percentage_of_candidate[name] = "{0:.3%}".format(votes_ct/total_votes)

    
    if votes_ct > winner_total:
        winner_total = votes_ct
        winner = name


print(f"Election Results")
print(f"--------------------------")
print(f"Total Votes: {total_votes}") 
print("--------------------------")
for name, votes_ct in can_votes.items():
    print(f"{name}: {percentage_of_candidate[name]} ({votes_ct})")    
print(f"--------------------------")
print(f"Winner: {winner}")
print(f"--------------------------")



print(f"Election Results", file=open("PyPoll_analysis.txt", "a"))
print(f"--------------------------", file=open("PyPoll_analysis.txt", "a"))
print(f"Total Votes: {total_votes}", file=open("PyPoll_analysis.txt", "a")) 
print("--------------------------")
for name, votes_ct in can_votes.items():
    print(f"{name}: {percentage_of_candidate[name]} ({votes_ct})", file=open("PyPoll_analysis.txt", "a"))    
print(f"--------------------------", file=open("PyPoll_analysis.txt", "a"))
print(f"Winner: {winner}", file=open("PyPoll_analysis.txt", "a"))
print(f"--------------------------", file=open("PyPoll_analysis.txt", "a"))

