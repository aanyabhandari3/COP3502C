gallons = float(input("Enter your water usage in gallons: "))


if gallons <= 5999:
    money = str(round((gallons/1000)*2.35,2))
    print("Money owed: $" + money)

elif (gallons <= 20000) and (gallons >= 6000):

    remainder = gallons - 5999
    m1 = (5999/1000)*2.35
    m2 = (remainder/1000)*3.75
    total = str(round((m1 + m2),2))

    print("Money owed: $" + total)
else:

    c1 = gallons - 20000
    m1 = (5999/1000)*2.35
    m2 = (14001/1000)*3.75
    m3 = (c1/1000)*6
    total = str(round((m1+m2+m3),2))

    print("Money owed: $" + total)