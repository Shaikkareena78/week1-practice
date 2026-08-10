seats = [
    "Available",
    "Booked",
    "Available",
    "Available",
    "Booked",
    "Available",
    "Booked",
    "Available"
]
total=0
booked=0
available=0
for i in range(1,len(seats)+1):
    print(" Seat",i,":",seats[i-1])
    total+=1
    if seats[i-1]=="Available":
        available+=1
    else:
        booked+=1
selected_num=int(input("select the seat no:"))
selected_seat=seats[selected_num-1]
if selected_seat=="Available":
    print("Seat booked successfully")
    selected_seat="Booked"
else:
    print("Seat is already booked")
print("Total Seats:",total)
print("Booked Seats:",booked)
print("Available Seats:",available)
