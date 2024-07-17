import csv

aircrafts = [["Medium Narrow Body",8,2650,180,8],
             ["Large Narrow Body",7,5600,220,10],
             ["Large Wide Body",5,4050,406,14]]

def main_menu():
    print("-------------------------------------------------------")
    print("Press A to enter airport details")
    print("Press F to enter flight details")
    print("Press P to enter price plan and to calculate the profit")
    print("Press C to clear data")
    print("Press Q to quit")
    print("-------------------------------------------------------")
    option = input("Enter: ").upper()
    if option == "Q":
        print("alr bye")
    elif option == "A":
        enter_airport_details()
    elif option == "F":
        enter_flight_details()

def enter_airport_details():
    airportCode = input("Enter the 3 character airport code (UK Only): ").upper()
    if airportCode != "LPL" and airportCode != "BOH":
        print("you suck")
        main_menu()
    overseasAirportCode = input("Enter the 3 character overseas airport code: ").upper()
    with open('airports.txt') as csv_file:
        reader = csv.reader(csv_file, delimiter=",")
        found=False
        for row in reader:
            if row[0] == overseasAirportCode:
                found=True
                print("")
                print(f"The airport is {row[1]}.")
                break
        if not(found):
            print("you suck")
        print("")
        main_menu()

def enter_flight_details():
    aircrafts = []
    print("Enter the aircraft type below")
    print("MN = medium narrow")
    print("LN = large narrow")
    print("LW = large wide")
    aircraft = input("Enter Here: ").lower()
    if aircraft=="mn":
        x=0
    elif aircraft=="ln":
        x=1
    elif aircraft=="lw":
        x=2
    print("Type of aircraft:", aircrafts[x][0])
    print("Running Cost:", aircrafts[x][1])
    print("Max Flight Range:", aircrafts[x][2])
    print("Capacity with all standard seats:", aircrafts[x][3])
    print("Min First Class Seats:", aircrafts[x][4])



main_menu()