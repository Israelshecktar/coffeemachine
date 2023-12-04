# Coffee Machine

A Python project that simulates a coffee machine and allows users to order different types of coffee.

## Description

This project is a command-line application that mimics the functionality of a real coffee machine. It can:

- Prompt the user to choose a drink from espresso, latte, or cappuccino.
- Check if there are enough resources to make the drink, such as water, milk, and coffee beans.
- Process the coins inserted by the user and check if the payment is sufficient.
- Make the coffee and dispense the change if any.
- Print a report of the current resources and money.
- Turn off the machine by entering a secret word.

The project uses object-oriented programming (OOP) to create a CoffeeMachine class that encapsulates the data and behavior of the coffee machine.

## Installation

To run this project, you need to have Python 3 installed on your system. You can download it from this web search result².

You also need to have a code editor or an IDE to edit and run the code. You can use any editor of your choice, such as Visual Studio Code, PyCharm, Sublime Text, etc.

To install the project, follow these steps:

- Clone the project repository from GitHub using this command:

```bash
git clone https://github.com/Israelshecktar/coffeemachine.git
```
- Run the main script using this command:

```bash
python3 coffeemachine.py
```

## Usage

To use the project, follow the instructions on the terminal. You will see a prompt like this:

```bash
What would you like? (espresso/latte/cappuccino/):
```

You can enter one of the drink options, or "report" to see the current resources and money, or "off" to turn off the machine.

If you choose a drink, the program will check if there are enough resources to make it. If not, it will print a message like this:

```bash
Sorry, there is not enough water.
```

If there are enough resources, the program will ask you to insert coins. You can enter the number of quarters, dimes, nickles, and pennies you have. For example:

```bash
Please insert coins.
How many quarters?: 2
How many dimes?: 1
How many nickles?: 0
How many pennies?: 3
```

The program will calculate the total amount of money you inserted and check if it is enough to buy the drink. If not, it will print a message like this:

```bash
Sorry, that's not enough money. Money refunded.
```

If it is enough, the program will make the coffee and give you the change if any. For example:

```bash
Here is $0.18 in change.
Here is your latte. Enjoy!
```

You can repeat the process until you enter "off" to turn off the machine.

Here is a screenshot of the project in action:

![Coffee Machine Screenshot](^3^)

## Contributing

This project is open for contributions. If you want to contribute, you can:

- Fork the project repository and create a new branch for your feature or bug fix.
- Write clear and concise commit messages and follow the coding style of the project.
- Test your code and make sure it works as expected.
- Create a pull request and describe the changes you made and why.
- Wait for the project maintainer to review and merge your pull request.

You can also report any issues or suggest new features by creating an issue on GitHub.

## License

This project is licensed under the MIT License. See the [LICENSE](^4^) file for more details.

