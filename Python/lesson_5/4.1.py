# Подвиг 1.
a, b = map(float, input().split())
if a > b:
    print(a)
else:
    print(b)

# Подвиг 2.
x = input().lower()
if x == x[::-1]:
    print("ДА")
else:
    print("НЕТ")

# Подвиг 3.
m, n = map(int, input().split())
if m % n == 0:
    print(int(m/n)) 
else:
    print(f"{m} на {n} нацело не делится")

# Подвиг 4.
a, b, c = map(int, input().split())
if c**2 == a**2 + b**2:
    print("ДА") 
else:
    print("НЕТ")

# Подвиг 5.
x = int(input())
if x % 10 == 7:
    print("ДА")
else:
    print("НЕТ")

# Подвиг 6.
x = input()
if 't' in x and 'h' in x and 'o' in x:
    print("ДА")
else:
    print("НЕТ")

# Подвиг 7.
s = input().split()
if "Москва" in s:
    s.remove("Москва")
print(*s)

# Подвиг 8.
a, b, c, d = map(int, input().split())
if ((a-1) > c and (b-1) > d) or ((a-1) > d and (b-1) > c):     
    print('ДА')
else:
    print('НЕТ')

# Подвиг 9.
n = list(map(int, input()))
if sum(n[:3]) == sum(n[-3:]):
    print("ДА")
else:
    print("НЕТ")

# Подвиг 10.
x = float(input())
if x % 5 < 3:
    print("green")
else:
    print("red")