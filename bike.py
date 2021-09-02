import datetime


class BikeRental:

    def __init__(self, stock=0, stock_name=[], checkout_list = []):
        """
        Our constructor class that instantiates bike rental shop.
        """

        self.stock = stock
        self.stock_name = stock_name
        self.checkout_list = checkout_list


    def createbike_byname(self,name):
        """
        Create bike and add to the list
        """
        self.stock_name.append(name)
        return None

    def displaystock(self):
        """
        Displays the bikes currently available for rent in the shop.
        """

        print("We have currently {} bikes available to rent.".format(self.stock))
        print(self.stock_name)
        print(self.checkout_list)
        return self.stock

    def add_bike(self, number):
        """
        Add new bikes in shop
        """
        self.stock += number
        return self.stock

    def checkout_bike(self,name,n):
        numb = self.stock_name.index(name)
        self.stock_name.pop(numb)
        counter = 1
        if len(self.checkout_list) != 0:
            checkout_tuple_l = [item for item in self.checkout_list if item[0] == name]
            if len(checkout_tuple_l) != 0:
                checkout_tuple_l_con = checkout_tuple_l[0]
                convert_checkout_tuple_l = list(checkout_tuple_l_con)
                if (name in convert_checkout_tuple_l):
                    self.checkout_list.pop(self.checkout_list.index(checkout_tuple_l_con))
                    counter = convert_checkout_tuple_l[1]
                    convert_checkout_tuple_l[1] = counter + 1
                    old_bike = tuple(convert_checkout_tuple_l)
                    self.checkout_list.append(old_bike)
                else:
                    self.checkout_list.append((name,counter))
            else:
                self.checkout_list.append((name, counter))
        else:
            self.checkout_list.append((name, counter))
        self.stock -= n

    def return_bike(self,name,number_of_bikes):
        self.stock_name.append(name)
        self.stock += number_of_bikes


    def rentBikeOnHourlyBasis(self, n):
        """
        Rents a bike on hourly basis to a customer.
        """
        if n <= 0:
            print("Number of bikes should be positive!")
            return None

        elif n > self.stock:
            print("Sorry! We have currently {} bikes available to rent.".format(self.stock))
            return None

        else:
            now = datetime.datetime.now()
            print("You have rented a {} bike(s) on hourly basis today at {} hours.".format(n, now.hour))
            print("You will be charged $5 for each hour per bike.")
            print("We hope that you enjoy our service.")

            self.stock -= n
            return now

    def rentBikeOnDailyBasis(self, n):
        """
        Rents a bike on daily basis to a customer.
        """
        if n <= 0:
            print("Number of bikes should be positive!")
            return None

        elif n > self.stock:
            print("Sorry! We have currently {} bikes available to rent.".format(self.stock))
            return None

        else:
            now = datetime.datetime.now()
            print("You have rented {} bike(s) on daily basis today at {} hours.".format(n, now.hour))
            print("You will be charged $20 for each day per bike.")
            print("We hope that you enjoy our service.")

            self.stock -= n
            return now

    def rentBikeOnWeeklyBasis(self, n):
        """
        Rents a bike on weekly basis to a customer.
        """
        if n <= 0:
            print("Number of bikes should be positive!")
            return None

        elif n > self.stock:
            print("Sorry! We have currently {} bikes available to rent.".format(self.stock))
            return None

        else:
            now = datetime.datetime.now()
            print("You have rented {} bike(s) on weekly basis today at {} hours.".format(n, now.hour))
            print("You will be charged $60 for each week per bike.")
            print("We hope that you enjoy our service.")
            self.stock -= n

            return now

    def returnBike(self, request):
        """
        1. Accept a rented bike from a customer
        2. Replensihes the inventory
        3. Return a bill
        """
        rentalTime, rentalBasis, numOfBikes = request
        bill = 0

        if rentalTime and rentalBasis and numOfBikes:
            self.stock += numOfBikes
            now = datetime.datetime.now()
            rentalPeriod = now - rentalTime

            # hourly bill calculation
            if rentalBasis == 1:
                bill = round(rentalPeriod.seconds / 3600) * 5 * numOfBikes

            # daily bill calculation
            elif rentalBasis == 2:
                bill = round(rentalPeriod.days) * 20 * numOfBikes

            # weekly bill calculation
            elif rentalBasis == 3:
                bill = round(rentalPeriod.days / 7) * 60 * numOfBikes

            if (3 <= numOfBikes <= 5):
                print("You are eligible for Family rental promotion of 30% discount")
                bill = bill * 0.7

            print("Thanks for returning your bike. Hope you enjoyed our service!")
            print("That would be ${}".format(bill))
            return bill
        else:
            print("Are you sure you rented a bike with us?")
            return None


class Customer:

    def __init__(self):
        """
        Our constructor method which instantiates various customer objects.
        """

        self.bikes = 0
        self.rentalBasis = 0
        self.rentalTime = 0
        self.bill = 0

    def requestBike(self):
        """
        Takes a request from the customer for the number of bikes.
        """

        bikes = input("How many bikes would you like to rent?")
        try:
            bikes = int(bikes)
        except ValueError:
            print("That's not a positive integer!")
            return -1

        if bikes < 1:
            print("Invalid input. Number of bikes should be greater than zero!")
            return -1
        else:
            self.bikes = bikes
        return self.bikes

    def returnBike(self):
        """
        Allows customers to return their bikes to the rental shop.
        """
        if self.rentalBasis and self.rentalTime and self.bikes:
            return self.rentalTime, self.rentalBasis, self.bikes
        else:
            return 0, 0, 0

