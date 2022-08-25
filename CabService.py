# Arrays
AC_Cars = ["ACC1-HONDA", "ACC2-AUDI", "ACC3-HYUNDAI", "ACC4-BMW"]
NonAC_Cars = ["NACC1-SUZUKI", "NACC2-SUZUKI", "NACC3-TATA"]
AC_Vans = ["ACV1-TOYOTA", "ACV2-TOYOTA", "ACV3-BENZ"]
NonAC_Vans = ["NACV1-TOYOTA", "NACV2-LANCER"]
ThreeWheels = ["TW1-BAJAJ", "TW2-BAJAJ", "TW3-BAJAJ", "TW4-BAJAJ"]
Trucks = ["TRK1-TATA", "TRK2-MITSUBISHI"]
Lorries = ["LRY1-TATA", "LRY2-MITSUBISHI"]
Hired_Vehicles = ["LRY3-TATA", "NACC4-BMW"]

# Global Functions
def msgReleaseSuccess():
    print(">>>>Vehicle Released Successfully<<<<")

def msgHireSuccess():
    print(">>>>Vehicle Hired Successfully<<<<")

def msgRemoveSuccess():
    print(">>>>Vehicle Removed Successfully<<<<")

def msgAddSuccess():
    print(">>>>Vehicle Added Successfully<<<<")

def back():
    x = input('''====================================
Enter (x) to Back : ''')
    if x == "x":
        print(mainMenuPage())
    else:
        print("Invalid Input!!!")

def back1():
    x = input('''====================================
Enter (x) to Back : ''')
    if x == "x":
        print(availableVehiclesPage())
    else:
        print("Invalid Input!!!")

def back2():
    x = input("Enter (x) to Back : ")
    if x == "x":
        print(addVehiclesPage())
    else:
        print("Invalid Input!!!")

def back3():
    x = input("Enter (x) to Back : ")
    if x == "x":
        print(removeVehiclesPage())
    else:
        print("Invalid Input!!!")

def back4():
    x = input("Enter (x) to Back : ")
    if x == "x":
        print(hireVehiclesPage())
    else:
        print("Invalid Input!!!")

# Option 7 Hired Vehicles List
def seeHiredVehiclesPage():
    print("==================================")
    print("        Hired Vehicles List       ")
    print("==================================")
    for h in Hired_Vehicles:
        print(h)
    print(back())

# Option 6 Release Hired Vehicles
def releaseHiredPage():
    print("=============================================")
    print("        *** Release Hired Vehicles ***       ")
    print("=============================================")
    print("=============================================")
    print("              Hired Vehicles List            ")
    print("=============================================")
    for h in Hired_Vehicles:
        print(h)
    print("=============================================")

    print("Enter (x) 2 Times to Back Menu")
    name = input('Enter Vehicle Name from List to Release: ')
    print("(1) Release " +name+ " to AC Cars")
    print("(2) Release " +name+ " to Non-AC Cars")
    print("(3) Release " +name+ " to AC Vans")
    print("(4) Release " +name+ " to Non-AC Vans")
    print("(5) Release " +name+ " to Three Wheels")
    print("(6) Release " +name+ " to Trucks")
    print("(7) Release " +name+ " to Lorries")
    print("=============================================")
    av = input('Enter a Choice: ')
    if av == "1":
        AC_Cars.append(name)
        Hired_Vehicles.remove(name)
        print(msgReleaseSuccess())
        print(back4())
    elif av == "2":
        NonAC_Cars.append(name)
        Hired_Vehicles.remove(name)
        print(msgReleaseSuccess())
        print(back4())
    elif av == "3":
        AC_Vans.append(name)
        Hired_Vehicles.remove(name)
        print(msgReleaseSuccess())
        print(back4())
    elif av == "4":
        NonAC_Vans.append(name)
        Hired_Vehicles.remove(name)
        print(msgReleaseSuccess())
        print(back4())
    elif av == "5":
        ThreeWheels.append(name)
        Hired_Vehicles.remove(name)
        print(msgReleaseSuccess())
        print(back4())
    elif av == "6":
        Trucks.append(name)
        Hired_Vehicles.remove(name)
        print(msgReleaseSuccess())
        print(back4())
    elif av == "7":
        Lorries.append(name)
        Hired_Vehicles.remove(name)
        print(msgReleaseSuccess())
        print(back4())
    elif av == "x":
        print(mainMenuPage())
    else:
        print("Invalid Input!!!")
        print(releaseHiredPage())


# Option 5 Hire Vehicles
def hireVehiclesPage():
    print("===========================")
    print("       Hire a Vehicle      ")
    print("===========================")
    print("(1) AC Cars")
    print("(2) Non-AC Cars")
    print("(3) AC Vans")
    print("(4) Non-AC Vans")
    print("(5) Three Wheels")
    print("(6) Trucks")
    print("(7) Lorries")
    print("===========================")
    print("(x) Back to Menu")
    av = input('Enter a Choice: ')
    if av == "1":
        for e in AC_Cars:
            print(e)
        a = str(input("Enter Car Name from List to Hire: "))
        AC_Cars.remove(a)
        Hired_Vehicles.append(a)
        print(msgHireSuccess())
        print(back4())
    elif av == "2":
        for e in NonAC_Cars:
            print(e)
        a = str(input("Enter Car Name from List to Hire: "))
        NonAC_Cars.remove(a)
        Hired_Vehicles.append(a)
        print(msgHireSuccess())
        print(back4())
    elif av == "3":
        for e in AC_Vans:
            print(e)
        a = str(input("Enter Van Name from List to Hire: "))
        AC_Vans.remove(a)
        Hired_Vehicles.append(a)
        print(msgHireSuccess())
        print(back4())
    elif av == "4":
        for e in NonAC_Vans:
            print(e)
        a = str(input("Enter Van Name from List to Hire: "))
        NonAC_Vans.remove(a)
        Hired_Vehicles.append(a)
        print(msgHireSuccess())
        print(back4())
    elif av == "5":
        for e in ThreeWheels:
            print(e)
        a = str(input("Enter Three Wheel Name from List to Hire: "))
        ThreeWheels.remove(a)
        Hired_Vehicles.append(a)
        print(msgHireSuccess())
        print(back4())
    elif av == "6":
        for e in Trucks:
            print(e)
        a = str(input("Enter Truck Name from List to Hire: "))
        Trucks.remove(a)
        Hired_Vehicles.append(a)
        print(msgHireSuccess())
        print(back4())
    elif av == "7":
        for e in Lorries:
            print(e)
        a = str(input("Enter Lorry Name from List to Hire: "))
        Lorries.remove(a)
        Hired_Vehicles.append(a)
        print(msgHireSuccess())
        print(back4())
    elif av == "x":
        print(mainMenuPage())
    else:
        print("Invalid Input!!!")
        print(hireVehiclesPage())


# Option 4 Remove Vehicles
def removeVehiclesPage():
    print("===========================")
    print("      Remove Vehicles      ")
    print("===========================")
    print("(1) AC Cars")
    print("(2) Non-AC Cars")
    print("(3) AC Vans")
    print("(4) Non-AC Vans")
    print("(5) Three Wheels")
    print("(6) Trucks")
    print("(7) Lorries")
    print("===========================")
    print("(x) Back to Menu")
    av = input('Enter a Choice: ')
    if av == "1":
        for e in AC_Cars:
            print(e)
        a = str(input("Enter Car Name from List to Remove: "))
        AC_Cars.remove(a)
        print(msgRemoveSuccess())
        for e in AC_Cars:
            print(e)
        print(back3())
    elif av == "2":
        for e in NonAC_Cars:
            print(e)
        a = str(input("Enter Car Name from List to Remove: "))
        NonAC_Cars.remove(a)
        print(msgRemoveSuccess())
        for e in NonAC_Cars:
            print(e)
        print(back3())
    elif av == "3":
        for e in AC_Vans:
            print(e)
        a = str(input("Enter Van Name from List to Remove: "))
        AC_Vans.remove(a)
        print(msgRemoveSuccess())
        for e in AC_Vans:
            print(e)
        print(back3())
    elif av == "4":
        for e in NonAC_Vans:
            print(e)
        a = str(input("Enter Van Name from List to Remove: "))
        NonAC_Vans.remove(a)
        print(msgRemoveSuccess())
        for e in NonAC_Vans:
            print(e)
        print(back3())
    elif av == "5":
        for e in ThreeWheels:
            print(e)
        a = str(input("Enter Three Wheel Name from List to Remove: "))
        ThreeWheels.remove(a)
        print(msgRemoveSuccess())
        for e in ThreeWheels:
            print(e)
        print(back3())
    elif av == "6":
        for e in Trucks:
            print(e)
        a = str(input("Enter Truck Name from List to Remove: "))
        Trucks.remove(a)
        print(msgRemoveSuccess())
        for e in Trucks:
            print(e)
        print(back3())
    elif av == "7":
        for e in Lorries:
            print(e)
        a = str(input("Enter Lorry Name from List to Remove: "))
        Lorries.remove(a)
        print(msgRemoveSuccess())
        for e in Lorries:
            print(e)
        print(back3())
    elif av == "x":
        print(mainMenuPage())
    else:
        print("Invalid Input!!!")
        print(addVehiclesPage())


# Option 3 Add Vehicles
def addVehiclesPage():
    print("===========================")
    print("      Add New Vehicles     ")
    print("===========================")
    print("(1) AC Cars")
    print("(2) Non-AC Cars")
    print("(3) AC Vans")
    print("(4) Non-AC Vans")
    print("(5) Three Wheels")
    print("(6) Trucks")
    print("(7) Lorries")
    print("===========================")
    print("(x) Back to Menu")
    av = input('Enter a Choice: ')
    if av == "1":
        a = str(input("Enter New AC Car Name: "))
        AC_Cars.append(a)
        print(msgAddSuccess())
        for e in AC_Cars:
            print(e)
        print(back2())
    elif av == "2":
        a = str(input("Enter New Non-AC Car Name: "))
        NonAC_Cars.append(a)
        print(msgAddSuccess())
        for e in NonAC_Cars:
            print(e)
        print(back2())
    elif av == "3":
        a = str(input("Enter New AC Van Name: "))
        AC_Vans.append(a)
        print(msgAddSuccess())
        for e in AC_Vans:
            print(e)
        print(back2())
    elif av == "4":
        a = str(input("Enter New Non-AC Van Name: "))
        NonAC_Vans.append(a)
        print(msgAddSuccess())
        for e in NonAC_Vans:
            print(e)
        print(back2())
    elif av == "5":
        a = str(input("Enter New Three Wheel Name: "))
        ThreeWheels.append(a)
        print(msgAddSuccess())
        for e in ThreeWheels:
            print(e)
        print(back2())
    elif av == "6":
        a = str(input("Enter New Truck Name: "))
        Trucks.append(a)
        print(msgAddSuccess())
        for e in Trucks:
            print(e)
        print(back2())
    elif av == "7":
        a = str(input("Enter New Lorry Name: "))
        Lorries.append(a)
        print(msgAddSuccess())
        for e in Lorries:
            print(e)
        print(back2())
    elif av == "x":
        print(mainMenuPage())
    else:
        print("Invalid Input!!!")
        print(addVehiclesPage())


# Option 2 See Available Vehicles
def availableVehiclesPage():
    print("===========================")
    print("     Available Vehicles    ")
    print("===========================")
    print("(1) AC Cars")
    print("(2) Non-AC Cars")
    print("(3) AC Vans")
    print("(4) Non-AC Vans")
    print("(5) Three Wheels")
    print("(6) Trucks")
    print("(7) Lorries")
    print("===========================")
    print("(x) Back to Menu")
    av = input('Enter a Choice: ')
    if av == "1":
        print("====================================")
        print("       AVAILABLE AC CARS LIST       ")
        print("====================================")
        for acc in AC_Cars:
            print(acc + " AC Car")
        print(back1())
    elif av == "2":
        print("====================================")
        print("     AVAILABLE NON-AC CARS LIST     ")
        print("====================================")
        for nacc in NonAC_Cars:
            print(nacc + " Non-AC Car")
        print(back1())
    elif av == "3":
        print("====================================")
        print("       AVAILABLE AC VANS LIST       ")
        print("====================================")
        for acv in AC_Vans:
            print(acv + " AC Van")
        print(back1())
    elif av == "4":
        print("====================================")
        print("     AVAILABLE NON-AC VANS LIST     ")
        print("====================================")
        for nacv in NonAC_Vans:
            print(nacv + " Non-AC Van")
        print(back1())
    elif av == "5":
        print("====================================")
        print("    AVAILABLE THREE WHEELS LIST     ")
        print("====================================")
        for twee in ThreeWheels:
            print(twee + " Three Wheel")
        print(back1())
    elif av == "6":
        print("====================================")
        print("       AVAILABLE TRUCKS LIST        ")
        print("====================================")
        for tru in Trucks:
            print(tru + " Truck")
        print(back1())
    elif av == "7":
        print("====================================")
        print("       AVAILABLE LORRIES LIST       ")
        print("====================================")
        for lor in Lorries:
            print(lor + " Lorry")
        print(back1())
    elif av == "x":
        print(mainMenuPage())
    else:
        print("Invalid Input!!!")
        print(availableVehiclesPage())


# Option 1 Vehicles Details
def detailsOfVehiclesPage():
    print("==================================================")
    print("                Vehicles Details                  ")
    print("==================================================")
    print("✔ Car | Passengers: 3 and 4 | Type: AC/ Non AC")
    print("✔ Van | Passengers: 6 and 8 | Type: AC/ Non AC")
    print("✔ Three Wheel | Passengers: 3")
    print("✔ Trucks | Size: 7 ft and 12 ft")
    print("✔ Lorry | Max Load - 2500kg and 3500kg")
    print("==================================================")
    print("Enter (x) to Go to Main Page:")
    e = input()
    if e == "x":
        print(mainMenuPage())
    else:
        print("Invalid Input!!!")
        print(detailsOfVehiclesPage())


# Main Page
def mainMenuPage():
    print("************************************")
    print("       Welcome to Cab Service       ")
    print("           BY M.T.M. ZAKIR          ")
    print("************************************")
    print("Choice 1 - Vehicles Details")
    print("Choice 2 - See Available Vehicles")
    print("Choice 3 - Add Vehicles")
    print("Choice 4 - Remove Vehicles")
    print("Choice 5 - Hire a Vehicle")
    print("Choice 6 - Release Hired Vehicles")
    print("Choice 7 - See Hired Vehicles List")
    print("************************************")
    x = input('Enter a Choice Number: ')
    print("************************************")
    if x == "1":
        print(detailsOfVehiclesPage())
    elif x == "2":
        print(availableVehiclesPage())
    elif x == "3":
        print(addVehiclesPage())
    elif x == "4":
        print(removeVehiclesPage())
    elif x == "5":
        print(hireVehiclesPage())
    elif x == "6":
        print(releaseHiredPage())
    elif x == "7":
        print(seeHiredVehiclesPage())
    else:
        print("Invalid Choice.... Please Try Again")

print(mainMenuPage())

