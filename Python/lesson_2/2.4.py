# Подвиг 1
a = 7
b = -4
c = 3
print(a,b,c)
# Подвиг 2
a = 7
b = -4
c = 3
print(a,b,c, sep='\n')
# Подвиг 3
s1 = "Hello"
s2 = "Balakirev"

print(s1, end=' ')
print(s2)
# Подвиг 4
s1, s2 = map(str.strip, input().split())

print(f"Word 1: {s1} | Word 2: {s2}")
# Подвиг 5
a,b = map(int, input().split())
print(a ** b)
# Подвиг 8
a,b = map(float, input().split())

print(a + b)
# Подвиг 9
x, y = map(int, input().split())

print(x + y + x * 2 + y * 4)
# Подвиг 10
a,b = float(input()), float(input())
print((a + b) * 2)
# Подвиг 11
import math
print(round(math.pi, 3))
# Подвиг 12
x = float(input())
print(f"Вы ввели число {x}")