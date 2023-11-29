class Pizza:
    def get_cost(self):
        raise NotImplementedError

class BasePizza(Pizza):
    def get_cost(self):
        return 10  # Base price

class Decorator(Pizza):
    def __init__(self, pizza):
        self._pizza = pizza

    def get_cost(self):
        return self._pizza.get_cost()

class Cheese(Decorator):
    def get_cost(self):
        return super().get_cost() + 2

class Peppers(Decorator):
    def get_cost(self):
        return super().get_cost() + 1.5

# Usage
pizza = BasePizza()
pizza_with_cheese = Cheese(pizza)
pizza_with_cheese_and_peppers = Peppers(pizza_with_cheese)
print(f"Total Cost: ${pizza_with_cheese_and_peppers.get_cost()}")
