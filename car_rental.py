import weakref

class Car():
  instances = []

  def __init__(self, carID, car_model, car_make, car_year, rental_price):
    self.__class__.instances.append(weakref.proxy(self))
    self.id = carID
    self.model = car_model
    self.make = car_make
    self.year = car_year
    self.rent = rental_price

  def display_cars(self):
        print(f"Car Model: {self.model.upper()}")
        print(f"Id: {self.id}")
        print(f"Car make: {self.make}")
        print(f"Year: {self.year}")
        print(f"Rent per day (in Rs): {self.rent}")
        print("----------")


  def get_price(self):
      return self.rent

class Customer():
  def __init__(self, ID, name, cars):
    self.cust_id = ID
    self.cust_name = name
    self.car_list = cars
    

class Car_Rental_System(Car):

  revenue = 0
  rented_list = []
  cars_available = 10
  
  CarList = [Car(1, 'abc', 'Land Rover', 2022, 2500), 
           Car(2, 'def', 'Toyota', 2020, 1600), 
           Car(3, 'ghi', 'Mahindra', 2021, 1200),
           Car(4, 'jkl', 'Honda', 2019, 1400),
           Car(5, 'mno', 'Suzuki', 2020, 1000),]
  def __init__(self):
    self.main_menu()


  def main_menu(self):
      option = str(input(""" 
      Welcome to Car Rental System!
      1. Display available cars for rent
      2. Rent a car
      3. Return a car
      4. Display the list of rented cars
      5. Display the total revenue 
      6. exit
      """))
      if option == '1':
        for instance in Car.instances:
            Car.display_cars(instance)
        self.main_menu()
      elif option == '2':
        self.rent_car()
      elif option == '3':
        self.return_car()
      elif option == '4':
        self.display_rented_cars()
        self.main_menu()
      elif option == '5':
        print(f"REvenue generated is {self.revenue}")
        self.main_menu()
      else:
        print("Thank you!")
        exit()


  def car_info(self):
    return self.CarList[(self.id)]

  def rent_car(self):
      self.ID = int(input("Enter your ID:"))
      self.num = int(input("Enter number of cars to be rented:"))

      if self.num >= 4:
       print("Oops! Atmost 3 cars can be rented.")
      elif self.num > self.cars_available:
       print(f"Sorry! {self.num} cars are not available at the moment.")
      else:
       for i in range(self.num):
         self.car = int(input("Enter the car ID:"))

         if self.CarList[self.car] in self.rented_list:
           print("Car already rented!")
           break
         else:
          self.days = int(input("For how many days do you want to rent?"))
          self.rented_list.append(self.CarList[self.car])
          self.cars_available = self.cars_available - 1
          self.revenue = self.revenue + (self.CarList[self.car].get_price())*self.days
       print("Car(s) rented successfully.")
      self.main_menu()

  def return_car(self):
    self.ID = int(input("Enter your ID:"))
    self.numcars= int(input("Enter ID of car to return:"))
    if self.CarList[self.numcars] in self.rented_list:
      self.no_of_cars_available = self.no_of_cars_available + 1
      self.rented_car_list.remove(self.CarList[self.numcars])
      print("Car returned successfully!")

    else:
      print("Car was not rented!")
    self.main_menu()
    
  def display_rented_cars(self):
    for i in self.rented_list:
      print(i)
    self.main_menu()

start = Car_Rental_System()
