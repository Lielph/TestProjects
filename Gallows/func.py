import random as rnd
from config import stages, words


def choose_word(list_of_words=words):
    return list_of_words[rnd.randint(0, len(list_of_words) - 1)].lower()


def start_game_print(word):
    # print(stages[0])
    print("".join(list("_" * len(word))), f"<-------------- загаданное слово из {len(word)} букв")
    return list("_" * len(word))


def reveal_letters(word: str, letter: str, reveal_word: list):
    index = [index for index, value in enumerate(word) if value == letter]
    for i in index:
        reveal_word[i] = letter
    return reveal_word


def game_function():
    used_letters = []
    chosen_word = choose_word()
    word = start_game_print(chosen_word)
    count = 10
    while "_" in word and count != 0:
        letter = input("Введите букву:")
        if letter in chosen_word:
            word = reveal_letters(chosen_word, letter, word)
            used_letters.append(letter)
            print("".join(word))
        else:
            count -= 1
            used_letters.append(letter)
            print(f"Такой буквы в слове нет"
                  f"\nСписок использованных букв {set(sorted(used_letters))}, оставшиеся жизни {count}")

    if count == 0:
        print("У вас кончились попытки")
    else:
        print(f"Вы победили, отгадав слово {chosen_word.upper()}")