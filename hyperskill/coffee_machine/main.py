WATER = 200
MILK = 50
COFFEE = 15

water = int(input("Write how many ml of water the coffee machine has:\n"))
milk = int(input("Write how many ml of milk the coffee machine has:\n"))
coffee = int(input("Write how many grams of coffee beans the coffee machine has:\n"))
cup_of_coffee = int(input("Write how many cups of coffee you will need:\n"))

available_water = water / WATER
available_milk = milk / MILK
available_coffee = coffee / COFFEE

available_cup_of_coffee = int(min(min(available_water, available_milk), available_coffee))
more_cup_of_coffee = available_cup_of_coffee - cup_of_coffee

if available_cup_of_coffee < cup_of_coffee:
    print(f"No, I can make only {available_cup_of_coffee} cups of coffee")
elif available_cup_of_coffee == cup_of_coffee:
    print("Yes, I can make that amount of coffee")
elif available_cup_of_coffee > cup_of_coffee:
    print(f"Yes, I can make that amount of coffee (and even {more_cup_of_coffee} more than that)")
