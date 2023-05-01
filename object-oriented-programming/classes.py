class Item:
    def calculate_price(self,x,y):
        return x*y



item1 = Item()
item1.name = "I phone"
item1.price = 100000
item1.quantity  = 10
ans1 = item1.calculate_price(item1.price*item1.quantity);
print(ans1)


item2 = Item()
item2.name = "Laptop"
item2.price = 100000
item2.quantity  = 2
ans2 = item1.calculate_price(item2.price*item2.quantity);
print(ans2);