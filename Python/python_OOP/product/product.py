class Product: 
    
    def __init__(self, price, item_name, weight, brand):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = "for sale"

        # def sell():
        #     if self.status
    def add_tax(self,tax):
        self.price=self.price+(self.price * tax)
        return self.price
    def sell(self,status):
        if status == "sold":
          self.status = "sold!"
    def return_item(self,x):
        if x == "defective":
          self.price = 0
          self.status = "defective"
          return
        elif x == "like_new":
          self.status = "for sale"
          return 
        elif x == "opened":
          self.status = "used"
          self.price = self.price*0.8
          return

    def display_info(self):
        return(f"Product's cost is {self.price}\nProduct's item name is {self.item_name}\nProduct's weight is {self.weight}\nProduct's brand is {self.brand}\nProduct's availability is {self.status}\n")

product1 = Product(5,"Apples",10,"Yup")
product2 = Product(7,"Oranges",3,"Yuppers")
product3 = Product(9,"Coffee",2,"Jopp")

print(product1.display_info())
product1.add_tax(0.45)
print(product1.display_info())
product1.sell("sold")
print(product1.display_info())
product1.return_item("like_new")
print(product1.display_info())
product1.return_item("opened")
print(product1.display_info())
product1.return_item("defective")
print(product1.display_info())
print(product2.display_info())
print(product3.display_info())
