# number_of_guests = int(input("Enter the number of friends joining (including you):\n"))
# guests_list = []
# if number_of_guests <= 0:
#     print("\nNo one is joining for the party")
# else:
#     print("\nEnter the name of every friend (including you), each on a new line:")
#     guests_list = [input() for _ in range(number_of_guests)]
#     print()
#     total = int(input("Enter the total bill value:\n"))
#     guests_dict = dict.fromkeys(guests_list, round(total / number_of_guests, 2))
#     print()
#     print(guests_dict)