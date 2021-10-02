import csv
import os

filename=os.path.join("PyPoll","Resources","PyPoll_Data.csv")
with open(filename, "r", newline='') as csvfile:

    #Initial Variables
    totalvotes = 0
    candidates={}
    winner=""
    winnervotes = 0
    
    #Initialize csvreader
    csvreader = csv.reader(csvfile,delimiter=',')

    #skip header
    next(csvreader)

    #create dictionary from data file
    for row in csvreader:
        #if candidate is already in dictionary
        if row[2] in candidates:
            candidates[row[2]] += 1

        #if candidate is missing from dictionary
        else:
            candidates[row[2]] = 1
        totalvotes += 1

print("Election Results")
print("-----------------------")
print(f"The total number of votes is {totalvotes}")
print("-----------------------")
for candidate in candidates:
    votepercent = "{:.3%}".format(candidates[candidate]/totalvotes)
    print(f"{candidate}: {votepercent} ({candidates[candidate]})")
    if candidates[candidate] > winnervotes:
        winnervotes = candidates[candidate]
        winner = candidate
print("-----------------------")
print(f"Winner: {winner}")
print("-----------------------")

with open("PyPoll/Analysis/output.txt", 'w', newline='') as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-----------------------\n")
    for candidate in candidates:
        votepercent = "{:.3%}".format(candidates[candidate]/totalvotes)
        txtfile.write(f"{candidate}: {votepercent} ({candidates[candidate]})\n")
    txtfile.write("-----------------------\n")
    txtfile.write(f"Winner: {winner}")
    txtfile.write("-----------------------")