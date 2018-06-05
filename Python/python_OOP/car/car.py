class Car:
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage 
        self.tax = 0.12

    def display_all(self):
      if self.price > 10000:
          self.tax = 0.15
      return(f"Price: {self.price}\nSpeed: {self.speed}\nFuel: {self.fuel}\nMileage: {self.mileage}\nTax: {self.tax}\n")
  
car1 = Car(2000,"35 mph","Full","15 mpg")
car2 = Car(2000,"5mph","Not Full","105 mpg")
car3 = Car(2000,"15mph","Kind of Full","95 mpg")
car4 = Car(2000,"25mph","Full","25 mpg")
car5 = Car(2000,"45mph","Empty","25 mpg")
car6 = Car(20000000,"35mph","Empty","15 mpg")

print(car1.display_all())
print(car2.display_all())
print(car3.display_all())
print(car4.display_all())
print(car5.display_all())
print(car6.display_all())
