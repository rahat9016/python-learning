class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y =  y
    
    def addition(self):
        return self.x + self.y
    

addition = Calculator(10, 20)
print(addition.addition())