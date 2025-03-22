speed=int(input("Enter the speed of the vehicle: "))
limit= 60
if speed>limit:
    fine= (speed-limit)*10
    print("Overspeeding, Fine is: ", fine)
else:
    print("Not overspeeding, drive safely")