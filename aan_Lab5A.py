import math 

def hex_char_decode(digit):
    decimal = 0   
    digit = digit.lower()               
    if (ord('0') <= ord(digit) and ord(digit) <= ord('9')):
        decimal = int(ord(digit) - ord('0'))
    elif (ord('a') <= ord(digit) and ord(digit) <= ord('f')):
        decimal = int(ord(digit) - ord('a')) + 10
    else:
        decimal = 0
    return decimal

def hex_string_decode(hex):
    decimal = 0

    for i in range(len(hex)):
        decimal *= 16
        decimal += hex_char_decode(hex[i])
    return decimal
    
def binary_string_decode(binary):
     decimal, i = 0, 0
     while(binary != 0):
            dec = int(binary) % 10
            decimal = decimal + dec * pow(2, i)
            binary = binary//10
            i += 1
            if binary == 0:
                return decimal

def binary_to_hex(binary):
    decimal = binary_string_decode(binary)
    hexaDeciNum = ['0'] * 100
    i = 0
    while(decimal != 0):
            counter = 0
            counter = decimal % 16
            if(counter < 10):
                hexaDeciNum[i] = chr(counter + 48)
                i = i + 1
            else:
                hexaDeciNum[i] = chr(counter + 55)
                i = i + 1
            decimal = int(decimal / 16)
    return hexaDeciNum, i

def main():
    while True:
        print("Decoding Menu\n-------------\n1. Decode hexadecimal\n2. Decode binary\n3. Convert binary to hexadecimal\n4. Quit\n")
        option = input("Please enter an option: ")

        if option == "1":
            original = input("Please enter the numeric string to convert: ").strip().upper() 
            if original[0:2] == "0X":
                modify = original[2:]
                new = hex_string_decode(modify)
                print("Result: " + str(int(new)) + '\n')
            else:
                new = hex_string_decode(original)
                print("Result: " + str(int(new)) + '\n')

        elif option == "2":
            original = input("Please enter the numeric string to convert: ").strip().upper() 
            if original[0:2] == "0B":
                modify = original[2:]
                new = binary_string_decode(int(modify))
                print("Result: " + str(int(new)) + '\n')
            else:
                new = binary_string_decode(int(original))
                print("Result: " + str(int(new)) + '\n')

        elif option == "3":
            original = input("Please enter the numeric string to convert: ").strip().upper() 
            if original[0:2] == "0B":
                modify = original[2:]
                hexaDeciNum, i = binary_to_hex(int(modify))
                j = i - 1
                print("Result: ", end="")
                while(j >= 0):
                    print((hexaDeciNum[j]), end="")
                    j = j - 1
                print()
            else:
                hexaDeciNum, i = binary_to_hex(int(original))
                j = i - 1
                print("Result: ", end="")
                while(j >= 0):
                    print((hexaDeciNum[j]), end="")
                    j = j - 1
                print()
        else:
            break


if __name__ == "__main__":
    main()