class Bike:
    def __init__(self, price, max_speed,miles):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def displayInfo(self):
      return(f"Bike's cost is {self.price}, bike's max speed is {self.max_speed}, the total miles on the bike are {self.miles}")
    def ride(self):
      print("Riding")
      self.miles+=10
      return self
    def reverse(self):
      if self.miles <= 0:
        print("can't reverse, 0 miles")
        return self
      else:
        print("Reversing")
        self.miles-=5
        return self

bike1 = Bike(200,"25mph",5)
bike2 = Bike(300,"35mph",10)
bike3 = Bike(400,"45mph",20)

print(bike1.ride().ride().ride().reverse().displayInfo())
print(bike2.ride().ride().reverse().reverse().displayInfo())
print(bike3.reverse().reverse().reverse().displayInfo())
