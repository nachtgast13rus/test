import text


def count_syllables(words):
    count = 0

    for word in words:
        word_count = count_syllables_in_word(word)
        count = count + word_count
    return count


def count_syllables_in_word(word):
    count = 0

    endings = ".,:;!?"
    last_char = word[:-1]
    if last_char in endings:
        processed_word = word[0:-1]
    else:
        processed_word = word

    if len(processed_word) <= 3:
        return 1
    vowels = "УуЕеАаОоЯяИиЮю"
    for char in processed_word:
        if char in vowels:
            count += 1
    return count


def count_sentences(text):
    count = 0
    terminals = ".!?"
    for i in text:
        if i in terminals:
            count += 1
    return count


def compute_readability(text):
    total_word = 0
    total_sentences = 0
    total_syllables = 0
    scores = 0

    total_word = len(text.split())
    total_sentences = count_sentences(text)
    total_syllables = count_syllables(text)
    print(total_word, total_sentences, total_syllables)

    scores = (206.835 - 1.015 * (total_word / total_sentences)
              - 84.6 * (total_syllables / total_word))

    print(scores)
compute_readability(text.text)
