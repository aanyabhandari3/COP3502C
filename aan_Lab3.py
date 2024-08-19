import math

counter = 0
total = 0
print("\nCurrent Result: 0.0")
while True:
    print("\nCalculator Menu")
    print("---------------")
    menu = int(input("0. Exit Program \n1. Addition \n2. Subtraction \n3. Multiplication \n4. Division \n5. Exponentiation \n6. Logarithm \n7. Display Average \n\nEnter Menu Selection: "))
    if menu not in [0,1,2,3,4,5,6,7]:
        print("\nError: Invalid selection!\n")
    else:
        if menu == 0:
            print("Thanks for using this calculator. Goodbye!")
            break
        else:
            if menu == 1:
                num1 = float(input("Enter first operand: "))
                num2 = float(input("Enter second operand: "))
                sum = num1 + num2
                print("\nCurrent Result: ",sum)
                total += sum
                counter += 1

            elif menu == 2:
                num1 = float(input("Enter first operand: "))
                num2 = float(input("Enter second operand: "))
                sum = num1 - num2
                print("\nCurrent Result: ",sum)
                total += sum
                counter += 1

            elif menu == 3:
                num1 = float(input("Enter first operand: "))
                num2 = float(input("Enter second operand: "))
                sum = num1*num2
                print("\nCurrent Result: ",sum)
                total += sum
                counter += 1

            elif menu == 4:
                num1 = float(input("Enter first operand: "))
                num2 = float(input("Enter second operand: "))
                sum = num1/num2
                print("\nCurrent Result: ",sum)
                total += sum
                counter += 1

            elif menu == 5:
                num1 = float(input("Enter first operand: "))
                num2 = float(input("Enter second operand: "))
                sum = num1**num2
                print("\nCurrent Result: ",sum)
                total += sum
                counter += 1

            elif menu == 6:
                num1 = float(input("Enter first operand: "))
                num2 = float(input("Enter second operand: "))
                sum = math.log(num2,num1)
                print("\nCurrent Result: ",sum)
                total += sum
                counter += 1

            else:
                if counter > 1:
                    avg = (total/(counter))
                    print("Sum of calculations: ", total)
                    print("Number of calculations: ",str(counter))
                    print("Average of calculations: ", round(avg,2))
                else:
                     print("Error: No calculations yet to average!")
                    
                    

        



