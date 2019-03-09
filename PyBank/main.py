#Import csv module
import csv

#Assigning filepaths to be used
csvpath = "budget_data.csv"
outputPath = "results.txt"

#Reading file and printing to teminal
with open(csvpath,newline="") as cvsfile:
    csvreader = csv.reader(cvsfile,delimiter = ',')
    #Skip the header row
    next(csvreader)

    #Initializing lists that will take values of months and profitLoss
    months = []
    profitLoss = []
    for row in csvreader:

        #Reading each row of cvs and appending values to lists
        months.append(row[0])
        profitLoss.append(int(row[1]))

    #Calculating and printing required values
    totalMonths = len(months)   
    print(f"Total months: {totalMonths}")

    netProfitLoss = sum(profitLoss)
    print(f"Total: {netProfitLoss}")

    averageProfitLoss = netProfitLoss/len(profitLoss)
    print(f"Average Change: {round(averageProfitLoss,2)}")

    greatestIncrease = max(profitLoss)
    increaseIndex = profitLoss.index(greatestIncrease)
    print(f"Greatest Increase in Profits: {months[increaseIndex]} {greatestIncrease}")


    greatestDecrease = min(profitLoss)
    decreaseIndex = profitLoss.index(greatestDecrease)
    print(f"Greatest Decrease in Profits: {months[decreaseIndex]} {greatestDecrease}")

    # Open text file and write results
    with open(outputPath, 'w') as text:
        text.write("Total Months: %s\n"%totalMonths)

        text.write("Total: %s\n"%netProfitLoss)

        text.write("Average Change: %s\n"%round(averageProfitLoss,2))

        text.write("Greatest Increase in Profits: %s"%months[increaseIndex])
        text.write(" %s\n"%greatestIncrease)

        text.write("Greatest Decrease in Profits: %s"%months[decreaseIndex])
        text.write(" %s\n"%greatestDecrease)

# #Printing and exporting text file with results
