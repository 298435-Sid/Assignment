class Pizza:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @classmethod
    def margherita(cls):
        return cls("Margherita", 10)

    @staticmethod
    def validate_topping(topping):
        healthy_toppings = ["pineapple", "mushroom", "tomato", "spinach", "onion"]
        return topping.lower() in healthy_toppings

my_pizza = Pizza.margherita()
is_valid = Pizza.validate_topping("pineapple")

print("Pizza ordered:", my_pizza.name)
print("Is topping valid?", is_valid)