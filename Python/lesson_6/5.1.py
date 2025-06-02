# Подвиг 2
n, m = map(int,input().split())
while n <= m:
    print(n ** 2, end = " " )
    n += 1

# Подвиг 3
price = float(input())
books = 2
while books <= 10:
    print(round(price * books, 1), end = " ")
    books += 1

# Подвиг 4
n = int(input())
i = 1
s = 0
while i <= n:
    s += 1 / i
    i += 1
print(round(s, 3))

# Подвиг 5
n = int(input())
s = 0
while n != 0:
    s += n
    n = int(input())
print(s)

# Подвиг 6
s = input()
while "--" in s:
    s = s.replace("--","-")
print(s)

# Подвиг 7
x = int(input())
p = 1
while x > 0:
    p *= x % 10
    x //= 10
print(p)

# Подвиг 8
n = int(input())
a, b = 1, 1
i = 1
while i <= n:
    print(a, end=" ")
    a, b = b, a + b
    i += 1

# Подвиг 9
n = int(input())
cells = 1
while n >= 3:
    cells *= 2
    n -= 3
print(cells)

# Подвиг 10
n = int(input())
i = 1
s = 1000
while i <= n:
    s *= 1.05
    i += 1
print(round(s, 2))

# Подвиг 11
n, m = map(int, input().split())
result = []
while n <= m:
    result.append(n * (n % 2))
    n += 1
print(' '.join(map(str, filter(None, result))))

# Подвиг 12
i = 100
while i <= 999:
    if i % 47 == 43 and i % 3 == 0:
        print(i, end=" ")
    i += 1