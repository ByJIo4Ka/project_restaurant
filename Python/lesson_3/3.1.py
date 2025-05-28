# Подвиг 4
s1 = input()
s2 = input()
print(s1 + ' ' + s2)

# Подвиг 7. 
s1, s2 = input().split()
print((s1 + ' ') * 2 + (s2 + ' ') * 3)

# Подвиг 8.
a, b = input().split()
print('Переменная a = ' + a + ', переменная b = ' + b)

# Подвиг 9. 
x = input()
print('Строка: ' + x + '. Длина: ' + str(len(x)))

# Подвиг 10.
x1, x2 = input().split()
print(x1 in x2, x1 == x2, x1 > x2, x1 < x2)

# Подвиг 11.
x1, x2 = input().split()
print(f"Коды: {x1} = {ord(x1)}, {x2} = {ord(x2)}")
