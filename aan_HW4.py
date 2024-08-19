from console_gfx import ConsoleGfx

def to_hex_string(data):
    res = ''.join('{:x}'.format(x) for x in data)
    return res

def count_runs(flat_data):
    counter = 0
    runs = encode_rle(flat_data)
    for i in range (0, len(runs), 2):
        count = int(runs[i])
        if count >= 15:
            counter += 1
        if count == 0:
            counter = 0
        if count < 15:
            counter += 1
    return counter

def encode_rle(flat_data):
    compressed = []
    count = 1
    for i in range (1, len(flat_data)):
        if flat_data[i] == flat_data[i - 1]:
            count+= 1
            if count >= 15:
                compressed.append(15)
                compressed.append(flat_data[i - 1])
                count = 0
        else:
            compressed.append(count)
            compressed.append(flat_data[i - 1])
            count = 1

    compressed.append(count)
    compressed.append(flat_data[-1])

    return compressed

def get_decoded_length(rle_data):
    count = 0
    for i in range (0, len(rle_data), 2):
        count += int(rle_data[i])
    
    return count

def decode_rle(rle_data):
    decompressed = []

    for i in range (0, len(rle_data), 2):
        count = rle_data[i]
        ch = rle_data[i +1]
        for j in range (0, count):
            decompressed.append(ch)
    return decompressed

def string_to_data(data_string):
    data = []
    for i in range(1, len(data_string)+1):
       hex = int(data_string[i-1], 16)
       data.append(hex)
    return data

def to_rle_string(rle_data):
    rle_string = []
    rle_final = ""
    for i in range(1, len(rle_data)+1):
        if i % 2 == 0:
            x = hex(rle_data[i-1])
            x = x[-1]
            rle_string.append(x)
            if i != (len(rle_data)):
                rle_string.append(":")
        else:
            rle_string.append(str(rle_data[i-1]))
    return (rle_final.join(rle_string))

def string_to_rle(rle_string):
    final = []
    x = rle_string.split(':')
    for i in range (0,len(x)):
        nothex = int((x[i][:-1]))
        final.append(nothex)
        hex = int(x[i][-1],16)
        final.append(hex)
    return final

def display_menu():
    print("\nRLE Menu\n"
        "--------")
    print("0. Exit")
    print("1. Load File")
    print("2. Load Test File")
    print("3. Read RLE String")
    print("4. Read RLE Hex String")
    print("5. Read Data Hex String")
    print("6: Display Image")
    print("7. Display RLE String")
    print("8. Display Hex RLE Data")
    print("9. Display Hex Flat Data")

def main():
    print("Welcome to the RLE image encoder! \n")
    print("Displaying Spectrum Image: ")
    ConsoleGfx.display_image(ConsoleGfx.test_rainbow)
    while True: 
        display_menu()
        option = int(input("\nSelect a Menu Option: "))
        if option == 0:
            break
        elif option == 1:
            file_name = input("Enter the name of the file: ")
            image_data = ConsoleGfx.load_file(file_name)
        elif option == 2:
            image_data = ConsoleGfx.test_image
            print("Test image data is loaded.")
        elif option == 3:
            enter = input("Enter an RLE string to be decoded: ")
            image_data = decode_rle(string_to_rle(enter))
        elif option == 4:
            enter = input("Enter the hex string holding RLE data: ")
            image_data = decode_rle(string_to_data(enter))
        elif option == 5:
            enter = input("Enter the hex string holding flat data: ")
            image_data = string_to_data(enter)
        elif option == 6:
            ConsoleGfx.display_image(image_data)
        elif option == 7:
            image_data = to_rle_string(encode_rle(image_data))
            print("RLE representation: ",image_data)
        elif option == 8:
            image_data = to_hex_string(encode_rle(image_data))
            print("RLE hex values: ",image_data)
        elif option == 9:
            image_data = to_hex_string(image_data)
            print("Flat hex values: ",image_data)
        else:
            print("Error! Invalid input.")

if __name__ == "__main__":
    main()