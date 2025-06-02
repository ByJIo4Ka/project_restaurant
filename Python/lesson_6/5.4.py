# Подвиг 1
text = input().lower()
res_count = 0
if 'ра' in text:
    for i in range(0, text.count('ра')):
        if 'ра' in text:
            res_count = text.find('ра', res_count if i == 0 else res_count + 1)
            print(res_count, end=' ')
else:
    print('-1')

# Подвиг 2
checked, p = list(), input()
checked.append(len(p) == 16 and p[1] == '7')
checked.append(p[0] + p[2] + p[6] + p[10] + p[13] == '+()--')
[checked.append(True if symbol in '0123456789' else False)
for index, symbol in enumerate(p)
if index in (3, 4, 5, 7, 8, 9, 11, 12, 14, 15)]
print('ДА' if all(checked) else 'НЕТ')

# Большой Подвиг 3
expression = input().strip()
c = 0
result = 0
i = 0
n = len(expression)
sign = 1
while i < n:
    char = expression[i]
    if char.isdigit():
        c = 0
        while i < n and expression[i].isdigit():
            c = c * 10 + int(expression[i])
            i += 1
        result += sign * c
    elif char == '+':
        sign = 1
        i += 1
    elif char == '-':
        sign = -1
        i += 1
    else:
        i += 1
print(result)

# Подвиг 4
numbers_list = list(map(int, input().split()))
for index, value in enumerate(numbers_list):
    numbers_list[index] = value ** 2
print(*numbers_list)

# Подвиг 5
numbers_list = list(map(str, input().split()))
string = ''
for index, value in enumerate(numbers_list):
    string += value + ' ' + value + " "
print(string)

# Подвиг 6
numbers_list = list(map(float, input().split()))
number = numbers_list[0]
for value in numbers_list:
    if number > value:
        number = value 
    else:
        continue
print(number)

# Подвиг 7
numbers_list = list(map(float, input().split()))
for index, value in enumerate(numbers_list):
    if value < 0:
        numbers_list[index] = -1.0
    else:
        continue
print(*numbers_list)