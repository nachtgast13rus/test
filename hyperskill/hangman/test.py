import random
import string

print('H A N G M A N')
lost = won = 0
while True:
    choice = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
    if choice == "play":

        def replace(let, enc):
            global word
            global letters
            enc = list(enc)
            i = 0
            while i < len(word):
                if word[i] == let:
                    enc[i] = let
                i += 1
            letters.add(let)
            return ''.join(enc)


        words = ('python', 'java', 'swift', 'javascript')
        word = random.choice(words)
        message = "You lost!"
        letters = set()
        encrypted = len(word) * '-'
        attempts = 0
        while attempts < 8:
            print('\n' + encrypted)
            letter = input('Input a letter:')
            if len(letter) <= 0 or len(letter) > 1:
                print("Please, input a single letter.")
            elif letter not in string.ascii_letters or letter in string.ascii_uppercase:
                print("Please, enter a lowercase letter from the English alphabet.")
            elif letter not in word:
                if letter in letters:
                    print("You've already guessed this letter")
                else:
                    print("That letter doesn't appear in the word.")
                    letters.add(letter)
                    attempts += 1
            elif letter in letters:
                print("You've already guessed this letter.")
            else:
                encrypted = replace(letter, encrypted)
            if encrypted == word:
                message = f"You guessed the word {encrypted}!\nYou survived!"
                break
        print(message)
        if message == "You lost!":
            lost += 1
        else:
            won += 1
    elif choice == "results":
        print(f"You won: {won} times.")
        print(f"You lost: {lost} times.")
    elif choice == "exit":
        break
