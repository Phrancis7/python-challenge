# Modules
import os
import csv

# activation from Francis's Mac downloads
budget_csv = os.path.join("bu/Users/francisokot/Downloads/Budget.csv")

with open('/Users/francisokot/Downloads/Budget.csv', newline='') as csvfile:
   csvreader=csv.reader(csvfile)
   header=next(csvreader)

# variables
   total_months=0
   total_pl=0.0
   average_total_pl=0
   change_monthly=0
   month_past=0
   total_change_month=0
   greatest_increase=0
   greatest_decrease=0
   date_1=str
   date_2=str
   
 
# Total profit/loss and total month total number of total_months Loop
   for row in csvreader:
      
# total Profit/loss sum
      total_pl+=int(row[1])
      total_months+=1

# average of "Profit/Losses" 
      average_total_pl=total_pl/(total_months)
      change_monthly=int(row[1])-month_past
      total_change_month=total_change_month+change_monthly
      month_past=int(row[1])

# greatest increase in profits 
      if greatest_increase< change_monthly:
         greatest_increase=change_monthly
         date_2=str(row[0])

# greatest decrease in losses
      if greatest_decrease>change_monthly:
         greatest_decrease=change_monthly
         date_1=str(row[0])

      
print("\nFinancial Analysis")
print("----------------------")
print()
print(f"Total Months: {total_months}")
print(f"Total: ${total_pl}")
print(f"Average: ${average_total_pl}")
print(f"Greatest increase in profit on {date_2} is ${greatest_increase}")
print(f"Greatest decrease in profit on {date_1} is ${greatest_decrease}\n")