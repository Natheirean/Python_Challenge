import os
import csv

with open("PyBank/Resources/budget_data.csv", 'r', newline='') as csvfile:

    #variables needed
    totalmonths=0
    netprofit=0


    #lists for forloop
    months=[]
    profit=[]

    #reading csv file
    csvreader = csv.reader(csvfile,delimiter=',')
    #Skip Header
    next(csvreader)

    #Store Data from File in lists created earlier
    for row in csvreader:
        months.append(row[0])
        profit.append(int(row[1]))
    
    #Calculate total months
    totalmonths=len(months)

    #Calculate Sum Profit/Loss
    i=0
    while i < len(profit):
        netprofit+=profit[i]
        i+=1
    
    #Calculate Averages List
    changes=[]
    j=0
    while j < len(profit)-1:
        changes.append(profit[j+1] - profit[j])
        j+=1
    averagechange = round(sum(changes)/len(changes),2)

    #Find Greatest Increase/Decrease Index in Change in Profits
    greatestincrease=max(changes)
    greatestdecrease=min(changes)
    increaseindex=changes.index(max(changes))
    decreaseindex=changes.index(min(changes))

    #use index to grab months for greatest increase/decrease
    greatestmonth = months[increaseindex+1]
    lowestmonth = months[decreaseindex+1]

with open("Pybank/output.txt", 'w', newline='') as txtfile:
    txtfile.write("Financial Analysis \n")
    txtfile.write("Total Months: ")
    txtfile.write(str(totalmonths))
    txtfile.write("\nAverage Change: $")
    txtfile.write(str(averagechange))
    txtfile.write("\nGreatest Increase in Profits: ")
    txtfile.write(greatestmonth)
    txtfile.write(" ($")
    txtfile.write(str(greatestincrease))
    txtfile.write(") \n")
    txtfile.write("Greatest Decrease in Profits: ")
    txtfile.write(lowestmonth)
    txtfile.write(" ($")
    txtfile.write(str(greatestdecrease))
    txtfile.write(")")