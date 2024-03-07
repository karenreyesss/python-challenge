import os
import csv

polldata=os.path.join('Resources', 'election_data.csv')

with open(polldata, newline="", encoding="utf-8") as csvfile:
    csvreader =csv.reader(csvfile, delimiter=",")

    next(csvreader)
    data=list(csvreader)
    row_count=len(data)

    candlist=[]
    tally = []
    for i in range (0,row_count):
        candidate = data[i][2]
        tally.append(candidate)
        if candidate not in candlist:
            candlist.append(candidate)
    candcount=len(candlist)

    votes=[]
    percentage=[]

    for j in range (0, candcount):
        name = candlist[j]
        votes.append(tally.count(name))
        vperc=votes[j]/row_count
        percentage.append(vperc)

    winner=votes.index(max(votes))

    #Print results

    print("Election Results")
    print("----------------------------")
    print(f"Total Votes: {row_count}")
    print("----------------------------")
    for k in range (0,candcount): 
        print(f"{candlist[k]}: {percentage[k]:.3%} ({votes[k]})")
    print("----------------------------")
    print(f"Winner: {candlist[winner]}")
    print("----------------------------")

  # Print the results to "PyPoll.txt" file
    
    output_file=os.path.join('Analysis', 'Election Results.txt')

    with open(output_file, 'w') as file:

        file.write("Election Results")
        file.write("\n")
        file.write("----------------------------")
        file.write("\n")
        file.write(f"Total Votes: {row_count}")
        file.write("\n")
        for k in range (0,candcount): 
            file.write(f"{candlist[k]}: {percentage[k]:.3%} ({votes[k]})")
            file.write("\n")
        file.write("----------------------------")
        file.write("\n")
        file.write(f"Winner: {candlist[winner]}")
        file.write("\n")
        file.write("----------------------------")




