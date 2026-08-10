customer_name = input("Enter customer name: ")
age = int(input("Enter age: "))
num_tickets = int(input("Enter number of tickets: "))

if 0 < age < 12:
    ticket_price = 120
elif 12 <= age <= 59:
    ticket_price = 200
elif age >= 60:
    ticket_price = 150

before_discount = num_tickets * ticket_price

if num_tickets >= 5:
    tickets_discount = before_discount * 0.10
else:
    tickets_discount = 0

after_discount = before_discount - tickets_discount

print("Customer Name:", customer_name)
print("Ticket Price:", ticket_price)
print("Number of Tickets:", num_tickets)
print("Total Before Discount:", before_discount)
print("Discount:", tickets_discount)
print("Final Amount:", after_discount)