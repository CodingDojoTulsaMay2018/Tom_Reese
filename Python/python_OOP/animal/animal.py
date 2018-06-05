class Animal:
  def __init__(self,name,health):
      self.name = name
      self.health = health 
  def walk(self,x):
      self.health-=(x*1)
      return self
  def run(self,x):
      self.health-=(x*5)
      return self
  def get_info(self):
      if self.health < 1:
        return(f"{self.name} is dead")
      else:
        return(f"{self.name}'s health is {self.health}")
class Dog(Animal):
    def __init__(self,name):
        super().__init__(name, health=150)
    def pet(self,x):
        self.health+=(x*5)
        return self
class Dragon(Animal):
    def __init__(self,name):
        super().__init__(name, health=170)
    def fly(self,x):
        self.health-=(x*10)
        return self
    def get_info(self):
      if self.health < 1:
        print(f"{self.name} is dead")
      return("I am a dragon")
class Beaver(Animal):
    def __init__(self,name):
        super().__init__(name, health=100)

animal1 = Animal("pancake",10)
print(animal1.get_info())
animal1.walk(2).run(2)
print(animal1.get_info())

dog1 = Dog("Flap Jack")
dog1.walk(50).run(4).pet(2)
print(dog1.get_info())

dragon1 = Dragon("Mike")
dragon1.fly(300)
print(dragon1.get_info())

beaver1 = Beaver("Martin")
print(beaver1.get_info())