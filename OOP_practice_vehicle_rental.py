import datetime

class VehicleRent():
    def __init__(self,stock):
        self.stock = stock
        self.now = 0

    def displayStock(self):
        print(self.stock, "Vehicle is available to rent.")
        return self.stock
    

    def rentHourly(self,n):
        if n <= 0:
            print("Please enter a valid number!")
            return None
        
        elif n > self.stock:
            print("Sorry, ", self.stock, "vehicle available to rent!")
            return None
        
        else:
            self.now = datetime.datetime.now()
            print(n, "vehicle rented hourly at ", self.now,".")

            self.stock = self.stock - n

            return self.now

    def rentDaily(self,n):
        if n <= 0:
            print("Please enter a valid number!")
            return None
        
        elif n > self.stock:
            print("Sorry, ", self.stock, "vehicle available to rent!")
            return None
        else:
            self.now = datetime.datetime.now()
            print(n, "vehicle rented hourly at ", self.now,".")

            self.stock = self.stock - n

            return self.now


    def returnVehicle(self,request,brand):
        car_h_price = 10
        car_d_price = car_h_price*8/10*24 
        bike_h_price = 5
        bike_d_price = bike_h_price*7/10*24

        rentalTime,rentalBasis, numOfVehicle = request
        bill = 0

        if brand == "car":
            if rentalTime and rentalBasis and numOfVehicle:
                self.stock += numOfVehicle
                now = datetime.datetime.now()
                rentalPeriod = now - rentalTime

                if rentalBasis == 1:
                    bill = rentalPeriod.seconds/3600*car_h_price*numOfVehicle
                
                elif rentalBasis == 2:
                    bill = rentalPeriod.seconds/(3600*24)*car_d_price*numOfVehicle

                if (2 <= numOfVehicle):
                    print("You hsve extra 20% discount")
                    bill = bill*0.8

                print("Thank you for returning your car")
                print("Price:", "$", bill )
                return bill
            
        if brand == "bike":
            if rentalTime and rentalBasis and numOfVehicle:
                self.stock += numOfVehicle
                now = datetime.datetime.now()
                rentalPeriod = now - rentalTime

                if rentalBasis == 1:
                    bill = rentalPeriod.seconds/3600*bike_h_price*numOfVehicle
                
                elif rentalBasis == 2:
                    bill = rentalPeriod.seconds/(3600*24)*bike_d_price*numOfVehicle

                if (2 <= numOfVehicle):
                    print("You have extra 20% discount")
                    bill = bill*0.8

                print("Thank you for returning your bike")
                print("Price:", "$", bill )
                return bill
        
        else:
            print("You do not rent a vehicle.")
            return None
        
class CarRent(VehicleRent):

    global discount_rate 
    discount_rate = 15

    def __init__(self,stock):
        super().__init__(stock)


    def discount(self,b):

        bill = b - (b * discount_rate) / 100
        return bill


class BikeRent(VehicleRent):
   
   def __init__(self,stock):
       super().__init__(stock)


class Customer:
    def __init__(self):
        self.bikes = 0
        self.rentalBasis_b = 0
        self.rentalTime_b = 0

        self.cars = 0
        self.rentalBasis_c = 0
        self.rentalTime_c = 0

    def requeestVehicle(self,brand):
        if brand == "bike":
            bikes = input("How many bikes would you like to rent?")

            try:
                bikes = int(bikes)
            except ValueError:
                print("Number should be Number")
                return -1
            
            if bikes < 1:
                print("Number of bikes should be greater than 0!")
                return -1
            else:
                self.bikes = bikes
                return self.bikes

        elif brand == "car":
            cars = input("How many cars would you like to rent?")

            try:
                cars = int(cars) 
            except ValueError:
                print("Number should be Number")
                return -1
            
            if cars < 1: 
                print("Number of cars should be greater than 0!")
                return -1
            else:
                self.cars = cars
                return self.cars

        else:
            print("Request vehicle error")
        

    def returnVehicle(self,brand):

        if brand == "bike":
            if self.rentalTime_b and self.rentalBasis_b and self.bikes:
                return self.rentalTime_b, self.rentalBasis_b, self.bikes
            else:
                return 0,0,0
            
        elif brand == "car":
            if self.rentalTime_c and self.rentalBasis_c and self.cars:
                return self.rentalTime_c, self.rentalBasis_c, self.cars
            else:
                return 0,0,0
            
        else:
            print("Return vehicle Error")



bike = BikeRent(100)
car = CarRent(10)
customer = Customer()

main_menu = True

while True:
    if main_menu:
        print("""
              ***** Vehicle Rental Shop *****
              A. Bike Menu
              B. Car Menu
              Q. Exit
              """)
        main_menu = False
        choice = input("Enter choice: ")
    
    
    if choice == "A" or choice == "a":
        print("""
              ***** BIKE MENU *****
              1. Display available bikes
              2. Request a bike on hourly basis $ 5
              3. Request a bike daily basis $ 84
              4. Return A bike
              5. Main Menu
              6. Exit
              """)
        choice = input("Enter choice: ")

        try:
            choice = int(choice)
        except ValueError:
            print("It is not integer")
            continue

        if choice == 1:
            bike.displayStock()
            choice = "A"
        elif choice == 2:
            customer.rentalTime_b = bike.rentHourly(customer.requeestVehicle("bike"))
            customer.rentalBasis_b = 1
            main_menu = True
            print("----------------")
        elif choice == 3:
            customer.rentalTime_b = bike.rentDaily(customer.requeestVehicle("bike"))
            customer.rentalBasis_b = 2
            main_menu = True
            print("----------------")
        elif choice == 4:
            customer.bill = bike.returnVehicle(customer.returnVehicle("bike"),"bike")
            customer.rentalBasis_b, customer.rentalTime_b, customer.bikes = 0,0,0
            main_menu = True
        elif choice == 5:
            main_menu = True
        elif choice == 6:
            break
        else:
            print("Invalid input, Please enter a number between 1-6 ")
            main_menu = True

    elif choice == "B" or choice == "b":
         print("""
              ***** CAR MENU *****
              1. Display available cars
              2. Request a cars on hourly basis $ 5
              3. Request a car daily basis $ 84
              4. Return A car
              5. Main Menu
              6. Exit
              """)
         choice = input("Enter choice: ")

         try:
            choice = int(choice)
         except ValueError:
            print("It is not integer")
            continue

         if choice == 1:
            car.displayStock()
            choice = "B"
         elif choice == 2:
            customer.rentalTime_c = car.rentHourly(customer.requeestVehicle("car"))
            customer.rentalBasis_c = 1
            main_menu = True
            print("----------------")
         elif choice == 3:
            customer.rentalTime_c = car.rentDaily(customer.requeestVehicle("car"))
            customer.rentalBasis_c = 2
            main_menu = True
            print("----------------")
         elif choice == 4:
            customer.cars = car.returnVehicle(customer.returnVehicle("car"),"car")
            customer.rentalBasis_c, customer.rentalTime_c, customer.cars = 0,0,0
            main_menu = True
         elif choice == 5:
            main_menu = True
         elif choice == 6:
            break
         else:
            print("Invalid input, Please enter a number between 1-6 ")
            main_menu = True
    
    elif choice == "Q" or choice == "q":
        break
    else:
        print("Invalid Input. Please Enter A-B-Q")
        main_menu = True

    print("Thank you for using vehicle rental shop")