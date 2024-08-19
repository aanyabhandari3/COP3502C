side1 = float(input("Enter side 1: "))
side2 = float(input("Enter side 2: "))
side3 = float(input("Enter side 3: "))

if (side1**2 + side2**2 == side3**2) or (side3**2 + side1**2 == side2**2) or (side3**2 + side2**2 == side1**2):
    print("This triangle has a right angle!")

else:
    print("This triangle doesn’t have a right angle...")