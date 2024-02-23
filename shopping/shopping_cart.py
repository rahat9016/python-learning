# 1. add item in cart
# 2. remove item from the cart by id, or name

class ShoppingCart:
    def __init__(self):
        self.items = []
    
    def getItems(self):
        return self.items

    def addItem(self, id, name, qty):
        item = (id, name, qty)
        self.items.append(item)
    
    def removeItem(self, id):
        for item in self.items:
            if(item[0] == id):
                self.items.remove(item)




shoppingCart = ShoppingCart()

shoppingCart.addItem(1, "Orange", 10)
shoppingCart.addItem(2, "Red", 10)
print(shoppingCart.getItems())
print(shoppingCart.removeItem(2))
print(shoppingCart.getItems())