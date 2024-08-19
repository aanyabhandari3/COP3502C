import sys
from heifer_generator import HeiferGenerator
from cow import Cow
from dragon import Dragon
from ice_dragon import IceDragon

def menu():
    print("Usage:\n python cowsay.py -l\npython cowsay.py MESSAGE\npython cowsay.py -n COW MESSAGE")

def list_cows(cows):
    print("Cows available: ", end = '')
    for c in cows:
        print(c.get_name(), end = '')
        print()
    pass

def find_cow(name, cows):
    for c in cows:
        if c.get_name() == name:
            return c
        else:
            print(f"Could not find {name} cow!")
            return

def main():
    if len(sys.argv) < 2:
        menu()
        return
    
    cows = HeiferGenerator.get_cows()
    if sys.argv[1] == '-l':
       list_cows(cows)

    elif sys.argv[1] == '-n':
        if len(sys.argv) < 4:
            print("Invalid arguments")
            menu()
        else:
            calf = find_cow(sys.argv[2], cows)
            print("".join(sys.argv[3:]), sys.argv[2])
            print(calf.get_image())
            print(calf)
            if isinstance(Cow, Dragon):
                if calf.can_breath_fire():
                    print("This dragon can breathe fire.")
                else:
                    print("This dragon cannot breathe fire.")
    else:
        print(calf[0].get_image())
        if isinstance(Cow, Dragon):
            if calf.can_breath_fire():
                print("This dragon can breathe fire.")
            else:
                print("This dragon cannot breathe fire.")


if __name__ == '__main__':
   main()