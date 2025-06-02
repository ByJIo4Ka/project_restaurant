# Подвиг 1
for i in range(11):
    print(i, end=" ")

# Подвиг 2
for i in range(-10, 1):
    print(i, end=" ")

# Подвиг 3
for i in range(-10, 0, 2):
    print(i, end=" ") 

# Подвиг 4
for i in range(1, 20, 3):
    print(i, end=" ") 

# Подвиг 5
list_num = list(map(int, input().split()))
result = 0
for i in list_num:
    if i % 2 != 0:
        result += i
print(result)

# Подвиг 6
list_word = list(map(str, input().split()))
list_num = []
for i in list_word:    
    list_num.append(len(i))
print(*list_num)

# Подвиг 7
n = int(input())
list_num = []
for i in range(1, n+1):
    if n % i == 0:
        print(i)

# Подвиг 8
n = int(input())
flag = True
for i in range(2, n // 2+1):
    if (n % i == 0):
        flag = False
if (flag):
    print("ДА")
else:   
    print("НЕТ")

# Подвиг 9
city = input().lower().split()
for i in range(len(city) - 1):
    if city[i].rstrip("ьъы")[-1] != city[i+1][0]:
        print("НЕТ")
        break
else:
    print("ДА")
    
# Подвиг 10
n = int(input())
total = 0
for i in range(n):
    if i % 3 == 0 or i % 5 == 0:
        total += i
print(total)