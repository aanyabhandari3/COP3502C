from console_gfx import ConsoleGfx

#ConsoleGfx.display_image(ConsoleGfx.test_rainbow)

def display_menu():
    print("\nRLE Menu\n"
        "---------------")
    print("0. Exit")
    print("1. Load File")
    print("2. Load Test File")
    print("6: Display Image")

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
            print("Test image data is loaded")
        elif option == 6:
            ConsoleGfx.display_image(image_data)

if __name__ == "__main__":
    main()

