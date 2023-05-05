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
            else:
                self.items[item] -= quantity
                print(f'{quantity} {item} have been removed from the cart')
        else:
                print(f'{item} that is not in the cart bro')
        

    def current_cart(self, item, quantity):
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
                    cart.current_cart(item, quantity)
            elif user_input == "quit":
                    break
            else:
                print("Try again later")

            print("Current cart:")
            for item, quantity in cart.items.items():
                print(f"{item} ({quantity})")

shopping_cart()

















