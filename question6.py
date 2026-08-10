expenses = [250, 1200, 450, 800, 150, 2000, 350]
total=0
exp_above=0
exp_below=0
for i in range(len(expenses)):
    total+=expenses[i]
    if expenses[i]>500:
        exp_above+=1
    else:
        exp_below+=1
avg=total/len(expenses)
print("Total Expense:",total)
print("Average Expense:",total/len(expenses))
print("Highest Expense:",max(expenses))
print("Lowest Expense:",min(expenses))
print("Number of Expenses Above ₹500:",exp_above)
print("Number of Expenses Below or Equal to ₹500:",exp_below)
print("Expenses Above Average:")
for i in range(len(expenses)):
    if expenses[i]>avg:
        print(expenses[i])