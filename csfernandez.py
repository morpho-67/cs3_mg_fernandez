class PizzaParlor:

    def __init__(self, price, topping, stock, topping_count):
        self.price = 10
        self.topping = 1.50
        self.stock = ["pepperoni", "mushroom", "extra"]
        self.topping_count = 0

    def calculate_total(self, topping_count):
        return self.topping * self.topping_count + self.price
    
