# Подвиг 2
p = [0] * 10
while p.count(1) < 5:
    i = int(input())
    if p[i] == 1:
        continue
    p[i] = 1
print(*p)

# Подвиг 3
p = 1
num = 1
while num != 0:
    num = int(input())
    if num <= 0:
        continue
    p *= num
print(p)

# Подвиг 4
city = input().split()
i = 0
while i < len(city):
    if len(city[i]) <= 5:
        print("НЕТ")
        break
    i += 1
else:
    print("ДА")

# Подвиг 5
num = list(map(str, input().split()))
count = 0
uslovie = ""
while count < len(num):
    word = num[count].lower()
    if word[0:1] == word[-1]:
        uslovie = "ДА"
        break
    elif word[0:1] != word[-1]:
        uslovie = "НЕТ"
    count += 1
print(uslovie)

# Подвиг 6
num = int(input())
string_numbers = list()
i = 1
while i <= num:
    if num >= 100:
        print("слишком большое значение n")
        break
    if i % 3 == 0 and i % 5 == 0:
        string_numbers.append(i)
    i+=1
print(*string_numbers)

# Подвиг 7
num = int(input())
count = 1
while True:
    if num < count**2:
        print(count)
        break
    else:
        count += 1

# Подвиг 8
x = int(input())
s = 10
i = 1
while s <= x:
    s += (s / 100 * 10)
    i += 1
else:
    print(i)
    
# Подвиг 9
import sys
lst_in = list(map(str.strip, sys.stdin.readlines()))
i = 0
while i < len(lst_in):
    if len(lst_in[i].split())<2:
        print(lst_in[i],end=' ')
    i += 1