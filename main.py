from bike import BikeRental, Customer

def main():
    shop = BikeRental(3,["Suzuki","Pulsar","TVS"])
    customer = Customer()

    while True:
        print("""
        ====== Bike Rental Shop =======
        1. Display available bikes
        2. Request a bike on hourly basis $5
        3. Request a bike on daily basis $20
        4. Request a bike on weekly basis $60
        5. Return a bike
        6. Add bikes
        7. Rent Bike Check
        8. Return
        9. Exit
        """)

        choice = input("Enter choice: ")

        try:
            choice = int(choice)
        except ValueError:
            print("That's not an int!")
            continue

        if choice == 1:
            shop.displaystock()

        elif choice == 2:
            customer.rentalTime = shop.rentBikeOnHourlyBasis(customer.requestBike())
            customer.rentalBasis = 1

        elif choice == 3:
            customer.rentalTime = shop.rentBikeOnDailyBasis(customer.requestBike())
            customer.rentalBasis = 2

        elif choice == 4:
            customer.rentalTime = shop.rentBikeOnWeeklyBasis(customer.requestBike())
            customer.rentalBasis = 3

        elif choice == 5:
            customer.bill = shop.returnBike(customer.returnBike())
            customer.rentalBasis, customer.rentalTime, customer.bikes = 0, 0, 0

        elif choice == 6:
            addbikes = input("Enter number of bikes: ")
            name = input("Enter new bike name:")
            shop.createbike_byname(name)
            shop.add_bike(int(addbikes))

        elif choice == 7:
            name = input("Bike name: ")
            bike = input("How many bikes would you like to rent?")
            shop.checkout_bike(name, int(bike))

        elif choice == 8:
            name = input("Bike name you want to return: ")
            bike = input("Number of bikes: ")
            shop.return_bike(name, int(bike))

        elif choice == 9:
            break
        else:
            print("Invalid input. Please enter number between 1-8 ")
    print("Thank you for using the bike rental system.")


if __name__ == "__main__":
    main()