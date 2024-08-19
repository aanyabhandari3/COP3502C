print("Available Currencies: A)USD B)CAD C)YEN")
amount = float(input("Enter transaction amount: "))
trans = input("Transaction currency: ")
convert = input("Currency to convert to: ")

if trans == convert:
    print("Conversion not needed...")

elif  trans == "A" and convert == "B":
   final = str(round(amount*1.24,2))
   print("Converted value: " + final + " CAD")

elif trans == "B" and convert == "C":
    final = str(round((amount/1.24)*108.59,2))
    print("Converted value: " + final + " YEN")

elif trans == "C" and convert == "B":
    final = str(round((amount/108.59)*1.24,2))
    print("Converted value: " + final + " CAD")

elif trans == "B" and convert == "A":
    final = str(round(amount/1.24,2))
    print("Converted value: " + final + " USD")

else:
    print("nope")