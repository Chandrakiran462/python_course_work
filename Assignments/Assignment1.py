#Zing Bus Ticket Booking

Boarding_point = input("Enter Boarding point: ")
Dropping_Point = input("Enter Dropping Point: ")
Date = input("Enter Date: ")
berth = input("Enter Berth(upper or lower): ")
bus = input("Enter Bus feature (AC or Non-AC): ")
seat_type = input("Enter Seat Type(Seater or Sleeper): ")
total_seats = int(input("Enter Total Seats: "))
seats_booked = int(input("Enter No.of Seats Booked: "))
seat_numbers = tuple(map(str,input("Enter Seat Number(s)(comma-seperated): ").split(',')))
amenities = list(map(str,input("Enter Bus amenities(comma-seperated): ").split(',')))
price = float(input("Enter Price: "))
discount = float(input("Enter Discount Percentage: "))
service_name = input()
driver_name = input()
driver_contact = input()


print("Zing Bus Journey Details".center(50,'-'))
print("Zing Bus Boarding Details".center(50,'-'))