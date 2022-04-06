WATER = 200
MILK = 50
coffee = 15

cup_of_coffee = int(input("Write how many cups of coffee you will need:\n"))
print(f'''For {cup_of_coffee} cups of coffee you will need:
{WATER * cup_of_coffee} ml of water
{MILK * cup_of_coffee} ml of milk
{coffee * cup_of_coffee} g of coffee beans''')
