# Class to represent the coffee machine
class CoffeeMachine:
    # Class attributes to store the resources and prices
    resources = {
        "water": 300, # in ml
        "milk": 200, # in ml
        "coffee": 100, # in g
        "money": 0 # in $
    }

    prices = {
        "espresso": 1.5, # in $
        "latte": 2.5, # in $
        "cappuccino": 3 # in $
    }

    # Resources required for each drink
    requirements = {
        "espresso": {
            "water": 50, # in ml
            "milk": 0, # in ml
            "coffee": 18 # in g
        },
        "latte": {
            "water": 200, # in ml
            "milk": 150, # in ml
            "coffee": 24 # in g
        },
        "cappuccino": {
            "water": 250, # in ml
            "milk": 100, # in ml
            "coffee": 24 # in g
        }
    }

    # Class method to print the report
    def print_report(self):
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")
        print(f"Money: ${self.resources['money']}")

    # Class method to prompt the user
    def prompt_user(self):
        # Ask the user what they want
        choice = input("What would you like? (espresso/latte/cappuccino/): ")
        # Return the user's choice
        return choice

    # Class method to check the resources
    def check_resources(self, drink):
        # Get the requirements for the drink
        req = self.requirements[drink]
        # Loop through the resources
        for resource in self.resources:
            # Check if there is enough resource
            if self.resources[resource] < req.get(resource, 0):
                # Print a message and return False
                print(f"Sorry, there is not enough {resource}.")
                return False
        # If there is enough of all resources, return True
        return True

    # Class method to process the coins
    def process_coins(self, drink):
        # Print a message to prompt the user to insert coins
        print("Please insert coins.")
        # Get the number of quarters, dimes, nickles and pennies from the user
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickles = int(input("How many nickles?: "))
        pennies = int(input("How many pennies?: "))
        # Calculate the total amount of money inserted
        total = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
        # Get the price of the drink
        price = self.prices[drink]
        # Check if the money is enough
        if total >= price:
            # Calculate the change and round it to two decimal places
            change = round(total - price, 2)
            # Print a message to give the change
            print(f"Here is ${change} in change.")
            # Add the price to the money resource
            self.resources["money"] += price
            # Make the coffee
            self.make_coffee(drink)
        else:
            # Print a message to refund the money
            print("Sorry, that's not enough money. Money refunded.")

    # Class method to make the coffee
    def make_coffee(self, drink):
        # Get the requirements for the drink
        req = self.requirements[drink]
        # Loop through the resources
        for resource in self.resources:
            # Deduct the required amount from the resource
            self.resources[resource] -= req.get(resource, 0)
        # Print a message to serve the drink
        print(f"Here is your {drink}. Enjoy!")

    # Class method to run the main loop of the program
    def run(self):
        # Loop until the user enters "off"
        while True:
            # Get the user's choice
            choice = self.prompt_user()
            # Check the user's choice
            if choice == "off":
                # Turn off the machine
                exit()
            elif choice == "report":
                # Print the report
                self.print_report()
            elif choice in self.prices:
                # Check the resources
                if self.check_resources(choice):
                    # If there are enough resources, process the coins
                    self.process_coins(choice)
            else:
                # Print an error message and ask again
                print("Invalid choice. Please try again.")


# Create an object of the CoffeeMachine class
machine = CoffeeMachine()
# Run the program
machine.run()
