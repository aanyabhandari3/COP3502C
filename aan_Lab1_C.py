m_line1 = float(input("Enter m for Line 1: "))
b_line1 = float(input("Enter b for Line 1: "))
m_line2 = float(input("Enter m for Line 2: "))
b_line2 = float(input("Enter b for Line 2: "))

x3_1 = round((b_line2-b_line1)/(m_line1-m_line2),2)
x3 = str(x3_1)

y3_1 = round(m_line1*x3_1 + b_line1,2)
y3 = str(y3_1)

print("The intersection point is: (" + x3 + ", " + y3 + ")")