vtype = str(input("Enter vehicle type(B:Bus/Truck, C:Car, S:Scooter/Cycle/Bike): "))
h  = int(input("Enter no. of hour parked:"))

truck = 20
car = 10
scooter= 5

if(vtype=='B' or vtype=='b'):
    print("Total parking charge for Truck/Bus: " , h*truck)
    
elif(vtype=='C' or vtype=='c'):
    print("Total parking charge for Cae=r: " , h*car)

elif(vtype=='S' or vtype=='s'):
    print("Total parking charge for Scooter: ", h*scooter)
    
else:
    print("Thanks for stopping by..")
