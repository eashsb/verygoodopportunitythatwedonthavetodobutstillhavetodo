def main_menu():
    print("Press A to enter airport details")
    print("Press F to enter flight details")
    print("Press P to enter price plan and to calculate the profit")
    print("Press C to clear data")
    print("Press Q to quit")
    print("-------------------------------------------------------")
    option = input("Enter: ")
    if option == "Q":
        print("alr bye")
    elif option == "A":
        enter_flight_details()

def enter_flight_details():
    airportCode = input("Enter the 3 character airport code (UK Only): ")
    if airportCode != "LPL" and airportCode != "BOH":
        print("you suck")
        main_menu()
    overseasAirportCode = input("Enter the 3 character overseas airport code: ")
    

main_menu()