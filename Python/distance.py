import math

x1,y1= input("Enter 1st point dimension:  ").split()
x2,y2= input("Enter 2nd point dimension:  ").split()


x1= float(x1)
x2= float(x2)
y1= float(y1)
y2= float(y2)



distance= (math.sqrt((x2-x1)**2 + (y2-y1)**2))

print("Distance: ",distance)
