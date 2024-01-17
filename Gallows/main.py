from func import *

Start_game = True
while True:
    q = input("Введите любое слово для начала игры"
              "\nдля завершения игры - нажми Enter")
    if not q:
        exit("Игра завершена")
    else:
        game_function()
