class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee_beans = 120
        self.disposable_cups = 9
        self.money = 550

    def __str__(self):
        print(f"""The coffee machine has:
{self.water} ml of water
{self.milk} ml of milk
{self.coffee_beans} g of coffee beans
{self.disposable_cups} disposable cups
${self.money} of money\n""")

    def make_espresso(self):
        """
        For one espresso, the coffee machine needs 250 ml of water and 16 g of coffee beans. It costs $4.
        :return:
        """
        if self.water >= 250 and self.coffee_beans >= 16 and self.disposable_cups >= 1:
            print("I have enough resources, making you a coffee!")
            self.water -= 250
            self.coffee_beans -= 16
            self.disposable_cups -= 1
            self.money += 4
        else:
            if self.water < 250:
                print("Sorry, not enough water!")
            if self.coffee_beans < 16:
                print("Sorry, not enough coffee beans!")
            if self.disposable_cups < 1:
                print("Sorry, not enough disposable cups!")

    def make_latte(self):
        """
        For a latte, the coffee machine needs 350 ml of water, 75 ml of milk, and 20 g of coffee beans. It costs $7.
        :return:
        """
        if self.water >= 350 and self.milk >= 75 and self.coffee_beans >= 20 and self.disposable_cups >= 1:
            print("I have enough resources, making you a coffee!")
            self.water -= 350
            self.milk -= 75
            self.coffee_beans -= 20
            self.disposable_cups -= 1
            self.money += 7
        else:
            if self.water < 350:
                print("Sorry, not enough water!")
            if self.milk < 75:
                print("Sorry, not enough milk!")
            if self.coffee_beans < 20:
                print("Sorry, not enough coffee beans!")
            if self.disposable_cups < 1:
                print("Sorry, not enough disposable cups!")

    def make_cappuccino(self):
        """
        And for a cappuccino, the coffee machine needs 200 ml of water, 100 ml of milk, and 12 g of coffee beans.
        It costs $6.
        :return:
        """
        if self.water >= 200 and self.milk >= 100 and self.coffee_beans >= 12 and self.disposable_cups >= 1:
            print("I have enough resources, making you a coffee!")
            self.water -= 200
            self.milk -= 100
            self.coffee_beans -= 12
            self.disposable_cups -= 1
            self.money += 6
        else:
            if self.water < 200:
                print("Sorry, not enough water!")
            if self.milk < 100:
                print("Sorry, not enough milk!")
            if self.coffee_beans < 12:
                print("Sorry, not enough coffee beans!")
            if self.disposable_cups < 1:
                print("Sorry, not enough disposable cups!")

    def buy(self):
        choice = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")
        if choice == "1":
            self.make_espresso()
        elif choice == "2":
            self.make_latte()
        elif choice == "3":
            self.make_cappuccino()


    def take_money(self):
        print(f"I gave you ${self.money}")
        self.money -= self.money

    def fill(self):
        self.water = self.water + int(input("Write how many ml of water you want to add:\n"))
        self.milk = self.milk + int(input("Write how many ml of milk you want to add:\n"))
        self.coffee_beans = self.coffee_beans + int(input("Write how many grams of coffee beans you want to add:\n"))
        self.disposable_cups = self.disposable_cups + int(input("Write how many disposable cups of coffee you want to "
                                                                "add:\n"))


def action():
    machine = CoffeeMachine()
    while True:
        answer = input("Write action (buy, fill, take, remaining, exit):\n")
        if answer == "buy":
            machine.buy()
        elif answer == "take":
            machine.take_money()
        elif answer == "fill":
            machine.fill()
        elif answer == "remaining":
            machine.__str__()
        elif answer == "exit":
            break


def main():
    action()


if __name__ == "__main__":
    main()
