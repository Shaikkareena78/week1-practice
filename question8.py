employee = ("Arjun", "Developer", 45000, 3)
employee_name,designation,salary,experience=employee
annual=salary*12
if experience<2:
    bonus=annual*0.05
elif experience>=2 and experience<=5 :
    bonus=annual*0.10
elif experience>5:
    bonus=annual*0.15
total=annual+bonus
print("Employee Name:",employee_name)
print("Designation:",designation)
print("Experience:",experience)
print("Monthly Salary:",salary)
print("Annual Salary:",annual)
print("Bonus:",bonus)
print("Total Annual Compensation:",total)





