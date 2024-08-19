print("Available movies today: ")
print("A)12 Strong: 1)2:30  2)4:40 3)7:50 4)10:50")
print("B)Coco:      1)12:40 2)3:45")
print("C)The Post:  1)12:45 2)3:35 3)7:05 4)9:55")

movie = input("Movie choice: ")
showtime = int(input("Showtime: "))

if movie.lower() not in ("a", "b", "c"):
     print("Invalid option; please restart app...")
else:
    if movie.lower() == "a":
        if showtime not in (1, 2, 3, 4):
            print("Invalid option; please restart app...")
        else:
            adult = int(input("Adult tickets: "))
            kid = int(input("Kid tickets: "))
            total = adult + kid
            if total <= 30:
                payment = (adult*12.45 + kid*9.68)
                print("Total cost: $",payment)
            else:
                print("Invalid option; please restart app...")
    elif movie.lower () == "b":
        if showtime not in (1, 2):
            print("Invalid option; please restart app...")
        else:
            if showtime == 1:
                adult = int(input("Adult tickets: "))
                kid = int(input("Kid tickets: "))
                total = adult + kid
                if total <= 30:
                    payment = (adult*11.17 + kid*8)
                    print("Total cost: $",payment)
                else:
                    print("Invalid option; please restart app...")
            else:
                adult = int(input("Adult tickets: "))
                kid = int(input("Kid tickets: "))
                total = adult + kid
                if total <= 30:
                    payment = (adult*12.45 + kid*9.68)
                    print("Total cost: $",payment)
                else:
                    print("Invalid option; please restart app...")
    else:
        if showtime not in (1, 2, 3, 4):
            print("Invalid option; please restart app...")
        else:
            if showtime == 1:
                adult = int(input("Adult tickets: "))
                kid = int(input("Kid tickets: "))
                total = adult + kid
                if total <= 30:
                    payment = (adult*11.17 + kid*8)
                    print("Total cost: $",payment)
                else:
                    print("Invalid option; please restart app...")
            else:
                adult = int(input("Adult tickets: "))
                kid = int(input("Kid tickets: "))
                total = adult + kid
                if total <= 30:
                    payment = (adult*12.45 + kid*9.68)
                    print("Total cost: $",payment)
                else:
                    print("Invalid option; please restart app...")
   