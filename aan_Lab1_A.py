R1 = float(input("What is the value of R1: "))
R2 = float(input("What is the value of R2: "))
R3 = float(input("What is the value of R3: "))

r = round((1/((1/R1)+ (1/R2)+(1/R3))),2)
R = str(r)

print("The equivalent resistance is " + R + " ohms")