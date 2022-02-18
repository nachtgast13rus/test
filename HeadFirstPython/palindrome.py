def palindrome(word):
    if len(word) <= 1:
        return True
    else:
        if word[0] == word[-1]:
            return palindrome(word[1:-1])
        else:
            return False


text = input("Enter your word please ")
if palindrome(text):
    print(f"{text} is palindrome")
else:
    print(f"{text} is not palindrome")
