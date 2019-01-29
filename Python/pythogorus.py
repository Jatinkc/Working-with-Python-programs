import math

base,perp=input("Enter Base and Perpendicular: ").split()

base=int(base)
base=base*base

perp=int(perp)
perp=perp*perp

hypot=base+perp



print("Hypotenuse",math.sqrt(hypot))


