import random

class PriceOfProduct:
    def id_of_product(self):
        first = random.randint(1, 100)
        second = random.randint(100, 200)
        return (first, second)


price = PriceOfProduct()

# price = PriceOfProduct().id_of_product()
print(price.id_of_product())