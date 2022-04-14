import random


def main():
    number_of_guests = int(input("Enter the number of friends joining (including you):\n"))
    if number_of_guests <= 0:
        print("\nNo one is joining for the party")
    else:
        print("\nEnter the name of every friend (including you), each on a new line:")
        guests_list = [input() for _ in range(number_of_guests)]
        print()
        total = int(input("Enter the total bill value:\n"))
        guests_dict = dict.fromkeys(guests_list, 0)
        choice_lucky = input("Do you want to use the 'Who is lucky?' feature? Write Yes/No:\n")
        if choice_lucky == "Yes":
            lucky_name = random.choice(list(guests_dict))
            print(f"\n{lucky_name} is the lucky one!\n")
            with_lucky = dict.fromkeys(guests_list, round(total / (number_of_guests - 1), 2))
            with_lucky[lucky_name] = 0
        else:
            print("\nNo one is going to be lucky")
            with_lucky = dict.fromkeys(guests_list, round(total / number_of_guests, 2))
        print(with_lucky)


if __name__ == "__main__":
    main()
