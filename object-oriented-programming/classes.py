class Item:
    def __init__(self,name: str,price: float,quantity):
        
        assert price >= 0
        assert quantity>=0


        self.name = name
        self.price = price
        self.quantity = quantity
    def calculate_price(self):
        return self.price*self.quantity

    

item1 = Item("I-phone",1000000,9)
#ans1 = item1.calculate_price(item1.price*item1.quantity);
print(item1.name," => ","price => ",item1.price, "quant => ", item1.quantity,"total price => ",item1.calculate_price())



item2 = Item()
item2.name = "Laptop"
item2.price = 100000
item2.quantity  = 2
ans2 = item1.calculate_price(item2.price*item2.quantity);
print(ans2);
