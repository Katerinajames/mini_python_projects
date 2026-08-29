import math
print("Calculation of the circumference of a circle")

def circumference_calc(r):
    c = 2 * r * math.pi
    return c

r = float(input("Insert the radius of the circle:\n"))
cir = circumference_calc(r)
print(f"The circumference of the given circle is {cir:.2f}")
