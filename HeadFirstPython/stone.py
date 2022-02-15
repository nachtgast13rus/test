import random

exit_choice = ""
while exit_choice != "n":
    comp_choice_list = ["камень", "ножницы", "бумага"]
    comp_choice = random.choice(comp_choice_list)
    print("Камень, ножницы, бумага. Компьютер сделал свой выбор.")
    player_choice = input("Введите свой: ")
    while player_choice not in comp_choice_list:
        print("Ошибка ввода, попробуйте еще раз.")
        player_choice = input("Введите свой: ")
    if comp_choice == player_choice:
        winner = "Ничья"
    elif comp_choice == "камень" and player_choice == "ножницы":
        winner = "Компьютер"
    elif comp_choice == "ножницы" and player_choice == "бумага":
        winner = "Компьютер"
    elif comp_choice == "бумага" and player_choice == "камень":
        winner = "Компьютер"
    else:
        winner = "Игрок"
    print(f"Вы выбрали {player_choice}, компьютер выбрал {comp_choice}, победил - {winner}")
    exit_choice = input("Нажмите n для выхода.")
