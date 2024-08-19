def isNumber(s):
    for char in s:
        if not char.isdigit():
            return False
    return True

title = input("Enter a title for the data: ")
print("You entered: "+title)
column1 = input("Enter the column 1 header: ")
print("You entered: "+column1)
column2 = input("Enter the column 2 header: ")
print("You entered: "+column2)

while True:
    data = input("Enter a data point (-1 to stop input):")
    if data == -1:
        break
    else:
        error1 = "Error: No comma in string."
        error2 = "Error: Too many commas in input."
        error3 = "Error: Comma not followed by an integer."
        first = data.split(",")
        print(first)
        number = first[1]
        if data.count(",") == 0:
            print(error1)
        elif data.count(",") > 1:
            print(error2)
        elif isNumber(number) == True:
            print(error3)
        else:
            print("Data string: ")
            print("Data integer: ")
        
