from pakuri import *
from pakudex import *

def display_menu():
    print("\nPakudex Main Menu\n"
        "-----------------")
    print("1. List Pakuri")
    print("2. Show Pakuri")
    print("3. Add Pakuri")
    print("4. Evolve Pakuri")
    print("5. Sort Pakuri")
    print("6. Exit")

def main():
    pakudex_instance = Pakudex()

    print("Welcome to Pakudex: Tracker Extraordinaire!")
    while True:
        size = input("Enter max capacity of the Pakudex: ")
        try:
            size = int(size)
            if size < 0:
                print("Please enter a valid size.")
            else:
                pakudex_instance.capacity = size
                print("The Pakudex can hold",size,"species of Pakuri.")
                break
        except ValueError:
            print("Please enter a valid size.")
            

    while True: 
        display_menu()
        while True:
            option = input("\nWhat would you like to do? ")
            try:
                option = int(option)
                break
            except ValueError:
                print("Unrecognized menu selection!")



        if option == 6:
            print("Thanks for using Pakudex! Bye!")
            break

        elif option == 1:
            if pakudex_instance.get_species_array() is None:
                print("No Pakuri in Pakudex yet!")
            else:
                print("Pakuri in Pakudex:")
                for x in range (0,len(pakudex_instance.get_species_array())):
                    print(f"{x+1}",". ",pakudex_instance.get_species_array()[x])
                
        elif option == 2:
            name = input("Enter the name of the species to display: ")
            if pakudex_instance.get_species_array() is None:
                print("Error: No such Pakuri!")
                continue
            else:
                if name in pakudex_instance.get_species_array():
                    print("Species: ",name)
                    print("Attack: ", pakudex_instance.get_stats(name)[0])
                    print("Defense: ", pakudex_instance.get_stats(name)[1])
                    print("Speed: ", pakudex_instance.get_stats(name)[2])
                    continue
                else:
                    print("Error: No such Pakuri!")
            continue

        elif option == 3:
            if size == pakudex_instance.get_size():
                    print("Error: Pakudex is full!")
            else:
                name = input("Enter the name of the species to add: ")
                if pakudex_instance.add_pakuri(name) == True:
                    print("Pakuri species",name,"successfully added!")
                else:
                     print("Pakudex already contains this species!")
            continue

        elif option == 4:
            name = input("Enter the name of the species to evolve: ")
            if pakudex_instance.get_species_array() is None:
                print("Error: No such Pakuri!")
            else:
                if name not in pakudex_instance.get_species_array():
                    print("Error: No such Pakuri!")
                    continue
                else:
                    if pakudex_instance.evolve_species(name) == True:
                        print(f"{name} has evolved!")
                continue

        elif option == 5:
            pakudex_instance.sort_pakuri()
            print("Pakuri have been sorted!")
        else:
            print("Unrecognized menu selection!")

if __name__ == "__main__":
    main()