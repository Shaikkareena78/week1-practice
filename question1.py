parking_hours=int(input("enter the parking hours:"))
parking_charge=0
service_charge=0
if parking_hours>=0 and parking_hours<=2:
    parking_charge=30*parking_hours
elif parking_hours>=0 and parking_hours<=2:
    parking_charge=25*parking_hours
elif parking_hours>=5:
    parking_charge=20*parking_hours
if parking_charge>150:
    service_charge=20
    parking_charge+=service_charge
final_amount=parking_charge+service_charge
print("Parking Charge:$",parking_charge)
print("Service Charge:$",service_charge)
print("Final Amount:$",final_amount)