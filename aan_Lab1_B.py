import math

length = float(input("Enter the length: "))
width = float(input("Enter the width: "))

peri = round((2*(length+width)),2)
perimeter = str(peri)

ar = round((length*width),2)
area = str(ar)

dia = round(math.sqrt(length ** 2 + width ** 2),2)
diagonal = str(dia)


print("Rectangle Perimeter: " + perimeter)
print("Rectangle Area: " + area)
print("Rectangle Diagonal: " + diagonal)