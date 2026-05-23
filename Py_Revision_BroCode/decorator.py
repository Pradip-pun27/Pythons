'''
Decorator : A function that extends the behavior of another function w/o
modifying the base function.
Pass the base function as an argument to the decorator.
'''

def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("You add Sprinkles :)")
        func(*args, **kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("You add Fudge :(")
        func(*args, **kwargs)
    return wrapper

@add_fudge
@add_sprinkles
def get_ice_cream(flavor):
    print(f"Here is your {flavor} Ice cream.")

get_ice_cream("Chocolate")
