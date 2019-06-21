# Modules
import os
import csv

# activation from Francis's Mac downloads
electioncsv = '/Users/francisokot/Downloads/election.csv'

# open csv
with open(electioncsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    # list variables
    total_votes = 0
    Khan_votes = 0
    Correy_votes = 0
    Li_votes = 0
    Tooley_votes = 0
    
    # start loop
    for row in csvreader:
    
        # row + total_votes
        total_votes = total_votes + 1
        
        # if the name in row[2] = Khan, then add to Khan_votes
        if row[2] == "Khan":
            Khan_votes = Khan_votes + 1
        
        # elif the name in row[2] = Correy, then add to Correy_votes
        elif row[2] == "Correy":
            Correy_votes = Correy_votes + 1
            
        # elif if the name in row[2] = Li, then add to Li_votes
        elif row[2] == "Li":
            Li_votes = Li_votes + 1
            
        # elif if the name in row[2] = O'Tooley, then add to Tooley_Votes
        elif row[2] == "O'Tooley":
            Tooley_votes = Tooley_votes + 1
        
            
    # highest votes
    if Khan_votes > Correy_votes:
        winner = "Khan"
    
    # converted to %
    pkhan_votes = (Khan_votes/total_votes) * 100
    pcorrey_votes = (Correy_votes/total_votes) * 100
    pli_votes = (Li_votes/total_votes) * 100
    ptooley_votes = (Tooley_votes/total_votes) * 100
        
print(f"Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
print(f"Khan: {pkhan_votes}% ({Khan_votes} votes)")
print(f"Correy: {pcorrey_votes}% ({Correy_votes} votes)")
print(f"Li: {pli_votes}% ({Li_votes} votes)")
print(f"O'Tooley: {ptooley_votes}% ({Tooley_votes} votes)")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")
