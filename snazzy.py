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
    elif option == "P":
        enter_price_plan_calc_profit()

def enter_airport_details():
    global airportCode,  overseasAirportCode
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
                print("Thanks, returning to menu now")
                break
        if not(found):
            print("you suck")
        print("")
        main_menu()

def enter_flight_details():
    global aircraft, firstClassSeats, standardClassSeats
    print("Enter the aircraft type below")
    print("MN = medium narrow")
    print("LN = large narrow")
    print("LW = large wide")
    print("-------------------------------------------------------")
    aircraft = input("Enter Here: ").lower()
    print("-------------------------------------------------------")

    if aircraft=="mn":
        x=0
    elif aircraft=="ln":
        x=1
    elif aircraft=="lw":
        x=2
    else:
        x=3
    if x!=3:
        print("Type of aircraft:", aircrafts[x][0])
        print("Running Cost:", aircrafts[x][1])
        print("Max Flight Range:", aircrafts[x][2])
        print("Capacity with all standard seats:", aircrafts[x][3])
        print("Min First Class Seats:", aircrafts[x][4])
        print("-------------------------------------------------------")
        firstClassSeats = int(input("Enter the number of first class seats on the plane: "))

        if firstClassSeats < aircrafts[x][4]:
            print("you suck, not enough first class seats entered")
        
        elif firstClassSeats > aircrafts[x][3] / 2:
            print("you suck, too many first class seats entered")
        else:
            standardClassSeats = aircrafts[x][3] - (firstClassSeats * 2)
            print("Thanks, returning to menu now")
    else:
        print("you suck")
    main_menu()

def enter_price_plan_calc_profit():
    if 'airportCode' and 'overseasAirportCode' in globals():
        if 'aircraft' in globals():
            if'firstClassSeats' in globals():
                if airportCode == "LPL":
                    
    else:
        print("Make sure to first enter you airport codes!")
    main_menu()

main_menu()