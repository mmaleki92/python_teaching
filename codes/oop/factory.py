class Pizza:
    def prepare(self):
        pass
    
    def bake(self):
        pass
    
    def cut(self):
        pass
    
    def box(self):
        pass

class CheesePizza(Pizza):
    def prepare(self):
        print("Preparing cheese pizza...")

    def bake(self):
        print("Baking cheese pizza...")

    def cut(self):
        print("Cutting cheese pizza...")

    def box(self):
        print("Boxing cheese pizza...")

class PepperoniPizza(Pizza):
    def prepare(self):
        print("Preparing pepperoni pizza...")

    def bake(self):
        print("Baking pepperoni pizza...")

    def cut(self):
        print("Cutting pepperoni pizza...")

    def box(self):
        print("Boxing pepperoni pizza...")

class PizzaFactory:
    def create_pizza(self, pizza_type):
        if pizza_type == "cheese":
            return CheesePizza()
        elif pizza_type == "pepperoni":
            return PepperoniPizza()
        else:
            raise ValueError(f"Invalid pizza type: {pizza_type}")

pizza_factory = PizzaFactory()
my_cheese_pizza = pizza_factory.create_pizza("cheese")
my_cheese_pizza.prepare()
my_cheese_pizza.bake()
my_cheese_pizza.cut()
my_cheese_pizza.box()

my_pepperoni_pizza = pizza_factory.create_pizza("pepperoni")
my_pepperoni_pizza.prepare()
my_pepperoni_pizza.bake()
my_pepperoni_pizza.cut()
my_pepperoni_pizza.box()