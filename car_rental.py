from IPython.utils.sysinfo import num_cpus

class Customer():
  def __init__(self, customer_ID, customer_name, list_of_rented_cars):
    self.custID = customer_ID
    self.cust_name = customer_name
    self.car_list = list_of_rented_cars
    
    def __str__(self):
      return "({}, {}, {})".format(self.custID, self.cust_name, self.car_list)
  

class Car():
  


  def __init__(self, carID, car_modal, car_make, car_year, rental_price):
    self.carID = carID
    self.modal = car_modal
    self.make = car_make
    self.year = car_year
    self.__price = rental_price


  def get_price(self):
      return self.__price


  def __str__(self):
    return ('Car ID: {}, Car Modal: {}, Car Make: {}, Car year: {}, Car Rental Price per day: {}'.format(self.carID, self.modal, self.make, self.year, self.get_price()))


class Car_Rental_System(Car):

  total_revenue = 0
  rented_car_list = []
  no_of_cars_available = 10
  
  CarList = [Car(0, 'A', 'Toyota', 2022, 1500), 
           Car(1, 'B', 'Toyota', 2022, 1600), 
           Car(2, 'C', 'Maruti', 2021, 1200),
           Car(3, 'D', 'Maruti', 2021, 1400),
           Car(4, 'E', 'Suzuki', 2020, 1000),
           Car(5, 'F', 'Suzuki', 2020, 1100),
           Car(6, 'G', 'Hyundai', 2019, 1600),
           Car(7, 'H', 'Hyundai', 2023, 2000),
           Car(8, 'I', 'Tata', 2020, 1200),
           Car(9, 'J', 'Tata', 2021, 1500)]
  def __init__(self):
    self.menu()


  def menu(self):
      user_input = input(""" 
      Welcome to Car Rental System!
      1. Display List of Available Cars for rent
      2. Rent a car
      3. Return a car
      4. Display the list of rented cars
      5. Display the total revenue generated
      6. Press any other key to exit
      """)
      if user_input == '1':
        self.display_available_cars()
      elif user_input == '2':
        self.rent_car()
      elif user_input == '3':
        self.return_car()
      elif user_input == '4':
        self.display_rented_cars()
        self.menu()
      elif user_input == '5':
        print("The revenue generated till current transaction is:", self.total_revenue)
        self.menu()
      else:
        print("Thanks for visiting! Have a good day !!")
        exit()

  def display_available_cars(self):
     for i in self.CarList:
       if i not in self.rented_car_list:
         print(i)
     self.menu()

  def car_info(self):
    return self.CarList[(self.carID)]

  def rent_car(self):
      self.ID = int(input("Enter your ID:"))
      self.name = input("Enter your name:")
      self.num = int(input("Enter the number of cars to be rented:"))

      if self.num > 3:
       print("Can't rent more than 3 cars at a time.")
      elif self.num > self.no_of_cars_available:
       print('Sorry! The number of given cars is currently unavailable.')
      else:
       for i in range(self.num):
         self.car = int(input("Enter the car ID:"))

         if self.CarList[self.car] in self.rented_car_list:
           print("Can't rent the car.")
           break
         else:
          self.days = int(input("Enter the number of days the cars has to be rented:"))
          self.rented_car_list.append(self.CarList[self.car])
          self.no_of_cars_available = self.no_of_cars_available - 1
          self.total_revenue = self.total_revenue + (self.CarList[self.car].get_price())*self.days
       print("Car(s) rented successfully.")
      self.menu()

  def return_car(self):
    self.ID = int(input("Enter your ID:"))
    self.name = input("Enter your name:")
    self.car_tobe_returned = int(input("Enter the ID of car you want to return:"))
    if self.CarList[self.car_tobe_returned] in self.rented_car_list:
      self.no_of_cars_available = self.no_of_cars_available + 1
      self.rented_car_list.remove(self.CarList[self.car_tobe_returned])
      print("Car returned successfully!")

    else:
      print("Can't return the given car.")
    self.menu()
    
  def display_rented_cars(self):
    for i in self.rented_car_list:
      print(i)
    self.menu()
    
obj = Car_Rental_System()
