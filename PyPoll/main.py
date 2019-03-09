#Import csv module
import csv

#Assign file paths
csvpath = "election_data.csv"
outputPath = "electionResults.txt"

with open(csvpath,newline="") as cvsfile:
    csvreader = csv.reader(cvsfile,delimiter = ',')

    next(csvreader)

    #Assign empty list to be appended 
    votes=[]

    for row in csvreader:

        #Appends the third column of csv (candidate names)
        votes.append(row[2])
    
    print("Election Results\n\n")
    print("--------------------------------")
    #Number of rows
    totalVotes = len(votes)
    print(f"Total Votes: {totalVotes}")

    print("--------------------------------")
    
    #The set function finds all unique elements in a list
    candidates = set(votes)
    #Convert set back into a list so the index method can be used later on
    candidates = list(candidates)

    percentages = []

    for candidate in candidates:
        percentage = round((votes.count(candidate)/totalVotes)*100,3)
        percentages.append(percentage)
        count =  votes.count(candidate)
        print(f"{candidate}: {percentage}% ({count})")
    
    print("--------------------------------")

    #Index of greatest percentage is the same as index of the winning candidate
    greatestPercentage = max(percentages)
    greatestIndex = percentages.index(greatestPercentage)
    print(f"Winner: {candidates[greatestIndex]}")

    print("--------------------------------")

     # Open text file and write results
    with open(outputPath, 'w') as text:
        #Here I zipped the candidates and their percentages together and converted the reult into a list
        #This allows me to print the candidates and their percentages in one go using a loop
        candidateZip = list(zip(candidates,percentages))
        text.write("Election Results\n\n")
        text.write("--------------------------------\n")

        text.write("Total Votes: %s\n"%totalVotes)

        text.write("--------------------------------\n")
        
        #loop for printing candidates and their percentages
        for candidate in candidateZip:
            percentage = round((votes.count(candidate[0])/totalVotes)*100,3)
            count =  votes.count(candidate[0])
            text.write("%s: "%candidate[0])
            text.write("%s %%"%percentage)
            text.write(" (%s)\n"%count)
        
        text.write("--------------------------------\n")

        text.write("Winner: %s"%candidates[greatestIndex])


