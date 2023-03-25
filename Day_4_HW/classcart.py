class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, item, quantity):
        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity
        print(f"{quantity} {item}(s) added to cart")

    def remove_item(self, item, quantity):
        if item in self.items:
            if quantity >= self.items[item]:
                del self.items[item]
                print(f"{item} removed from cart")

    def current_cart(self, item):
        if item in self.items:
            print(f"{item} ({self.items[item]})")

def shopping_cart():
    cart = ShoppingCart()
    while True:
        user_input = input("Enter 'add', 'remove', 'cart', or 'quit': ")
        if user_input == "add":
            item = input("What would you like to add?: ")
            quantity = int(input("How many?: "))
            cart.add_item(item, quantity)
        elif user_input == "remove":
            item = input("What would you like to remove?: ")
            quantity = int(input("How many?: "))
            cart.remove_item(item, quantity)
        elif user_input == "cart":
            cart.check_item(item)
        elif user_input == "quit":
            break
        else:
            print("Try again later")

    print("Current cart:")
    for item, quantity in cart.items.items():
        print(f"{item} ({quantity})")

shopping_cart()




#Write a Python class which has two methods get_String and print_String. get_String 
#accept a string from the user and print_String print the string in upper case


class String():
    def __init__(self):
        self.string = " "

def get_String(self):
        self.string = input("Type a string hurry!: ")

def print_String(self):
        print(self.string.upper())
    
#Does not work yet, missing 1 required positional argument 'self'?????WTF
get_String()
print_String()







