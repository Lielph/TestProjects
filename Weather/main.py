from func import *
print("*" * 75)
print("""*Для того чтобы узнать погоду введи запрос в формате city[,country_code]
*Для того чтобы выйти из программы нажми Enter""")
print("*" * 75)
while True:
    q = input("Введи название города:")
    if not q:
        print("До встречи, всего хорошего!")
        break
    else:
        weather = get_weather(q)
        print_weather(weather)
        save_excel(weather)
