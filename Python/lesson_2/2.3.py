# ввод целого числа
d = int(input())

# здесь продолжите программу
print(abs(d))

# ввод целого числа
d1, d2, d3, d4, d5 = map(int, input().split())

# здесь продолжите программу
print(min(d1,d2,d3,d4,d5))

# ввод целого числа
d1, d2, d3, d4, d5 = map(int, input().split())

# здесь продолжите программу
print(max(d1,d2,d3,d4,d5))

# ввод данных
a, b = map(int, input().split())

# здесь продолжите программу
print(round((a ** 2 + b ** 2) ** 0.5, 2))

# ввод данных
import math
n, k = map(int, input().split())

# здесь продолжите программу
print(int(math.factorial(n) / (math.factorial(k) * math.factorial(n - k))))

# ввод данных
n, m = map(int, input().split())
import math
# здесь продолжите программу
print(math.ceil((n + m) / 20))

# ввод данных
x = int(input())
import math
# здесь продолжите программу
print(math.floor(500 / (x * 0.9)))