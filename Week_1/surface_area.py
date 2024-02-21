
#This is a programme to solve surface area of cone
import math


r=float(input("enter radius: ")) 
h=float(input("enter height: ")) 

circles=(2 * math.pi * r**2)
curved=(math.pi * 2 * h)
surface_area=(circles + curved)

print("the surface area of cylinder",surface_area)

#This is a programme to solve surface area of sphere
import math

r=float(input("enter radius: ")) 
curve=(4 * math.pi* r** 2)
print("the surface area of a sphere", curve)



