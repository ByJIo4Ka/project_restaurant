# Подвиг 1.
name = input()
last_name = input()
age = input()
print("Уважаемый {0} {1}! Поздравляем Вас с {2}-летием!".format(name, last_name, age))

# Подвиг 2.
width, depth, height = input().split()
print("Габариты: {a} x {b} x {c}".format(a = width, b = depth, c  = height))

# Подвиг 3.
a, b = map(int, input().split())
print(f"{min(a, b)} {max(a, b)}")

# Подвиг 4.
city = input()
street = input()
number_house = input()
number_appartment = input()
print(f"г. {city}, ул. {street}, д. {number_house}, кв. {number_appartment}")

# Подвиг 5.
dollar_rate, rubles = float(input()), int(input())
print(f"Вы можете получить {int(rubles // dollar_rate)}$ за {rubles} рублей по курсу {dollar_rate}")