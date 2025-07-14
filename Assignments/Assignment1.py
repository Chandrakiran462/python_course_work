#Zing Bus Ticket Booking

Boarding_point = input("Enter Boarding point: ")
Dropping_point = input("Enter Dropping Point: ")
Date = input("Enter Date of Journey: ")
berth = input("Enter Berth(upper or lower): ")
bus = input("Enter Bus feature (AC or Non-AC): ")
seat_type = input("Enter Seat Type(Seater or Sleeper): ")
total_seats = int(input("Enter Total Seats: "))
seats_booked = int(input("Enter No.of Seats Booked: "))
seat_numbers = tuple(map(str,input("Enter Seat Number(s)(comma-seperated): ").split(',')))
amenities = list(map(str,input("Enter Bus amenities(comma-seperated): ").split(',')))
price = float(input("Enter Price: "))
discount = float(input("Enter Discount Percentage: "))
service_name = input("Enter Service Name: ")
driver_name = input("Enter Driver Name: ")
driver_contact = input("Enter Driver Contace: ")


print("Zing Bus Journey Details".center(50,'-'))
print(f"Date: {Date} \nTrip: {Boarding_point} to {Dropping_point} \nseat number(s) : {seat_numbers}")
print("Zing Bus Ticket Details".center(50,'-'))
print("berth ,bus, seat type, seat number(s): ",berth,bus,seat_type,seat_numbers,sep=',')
print("Zing Bus price Details".center(50,'-'))
print("price : %.2f \nDiscount: %.2f " % (price,discount))
print("Zing Bus Driver Details".center(50,'-'))
print("Driver Name: {} \nDriver Contact: {}".format(driver_name,driver_contact))




#OUTPUT

# [INPUT]
# Enter Boarding point: Rajanagaram
# Enter Dropping Point: Hyderabad  
# Enter Date of Journey: 28-7-2025
# Enter Berth(upper or lower): upper
# Enter Bus feature (AC or Non-AC): AC
# Enter Seat Type(Seater or Sleeper): Sleeper
# Enter Total Seats: 36
# Enter No.of Seats Booked: 8
# Enter Seat Number(s)(comma-seperated): S17,S18
# Enter Bus amenities(comma-seperated):  Air Freshener, Charging Point, Medical Kit, water Bottle, Live Tracking, Blanket 
# Enter Price: 586.35
# Enter Discount Percentage: 15
# Enter Service Name: Zing bus Plus
# Enter Driver Name: Raju
# Enter Driver Contace: 7584689533


# [OUTPUT]
# -------------Zing Bus Journey Details-------------
# Date: 28-7-2025
# Trip: Rajanagaram to Hyderabad
# seat number(s) : ('S17', 'S18')
# -------------Zing Bus Ticket Details--------------
# berth ,bus, seat type, seat number(s): ,upper,AC,Sleeper,('S17', 'S18')
# --------------Zing Bus price Details--------------
# price : 586.35
# Discount: 15.00
# -------------Zing Bus Driver Details--------------
# Driver Name: Raju
# Driver Contact: 7584689533