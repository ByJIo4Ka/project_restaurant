# Подвиг 1.
N = int(input())
a =  [[1] * N for i in range(N)]
b = a[0]
b[-1] = 5
while N != 0:
    print(*b)
    N -= 1

# Подвиг 2.
import sys
lst_in = list(map(str.strip, sys.stdin.readlines()))
for string_word in lst_in:  
    while '  ' in string_word:
        string_word = string_word.replace('  ', ' ')
    print(string_word.replace(' ','-'))

# Подвиг 3.
n = int(input())            
nums = list(range(n))
nums[1] = 0
i = 2
while i < n ** 0.5:
    if nums[i] != 0:
        j = i ** 2
        while j < n:             
            nums[j] = 0
            j += i
    i += 1
nums = [num for num in nums if num != 0]
print(*nums)

# Подвиг 4.
import sys
s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]
string_matrix = len(lst_in[0])
flag = True
lst_in = [[0]*string_matrix] + (lst_in) + [[0]*string_matrix]
for i in range(len(lst_in)):
    lst_in[i].insert(0, 0)
    lst_in[i].append(0)
for index_str, value in enumerate(lst_in):
    if flag == True:
        for index_positon, value_str in enumerate(value):
            if value_str == 1:
                if (lst_in[index_str][index_positon + 1] == 1 or lst_in[index_str][index_positon - 1] == 1):
                    flag = False
                    break
                if 1 in lst_in[index_str - 1][index_positon - 1: index_positon +1]:
                    flag = False
                    break
                if 1 in lst_in[index_str + 1][index_positon - 1: index_positon +1]:
                    flag = False
                    break
                else:
                    flag = True
    else:
        break
if flag: 
    print("ДА")
else:
    print("НЕТ")

# Подвиг 5.
import sys
s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]
flag = True
count = 1
for index_1 in range(0, len(lst_in)): 
    for index_2 in range(count, len(lst_in)):
 
        number_1 = lst_in[index_1][index_2]
        number_2 = lst_in[index_2][index_1]
        if number_1 != number_2:
            flag = False
            break
        else:
            flag = True
    if flag == False:
        break
if flag:
    print("ДА")
else:
    print("НЕТ")

# Большой подвиг 6.
number_lst = list(map(int, input().split()))
count = 1
for index_1 in range(0, len(number_lst)):
    for index_2 in range(count, len(number_lst)):
        number_1 = number_lst[index_1]           
        number_2 = number_lst[index_2]           
        if number_1 > number_2:               
            number_mid = number_lst[index_1]      
            number_lst[index_1] = number_lst[index_2]
            number_lst[index_2] = number_mid     
 
    count += 1
print(*number_lst)

# Большой подвиг 7.
number_lst = list(map(int, input().split()))
count = 0 
for index in range(0, len(number_lst)):
    count = 0
    for index_2 in range(1, len(number_lst)):
        if number_lst[count] > number_lst[index_2]: 
            number_lst[count], number_lst[index_2] = number_lst[index_2], number_lst[count]
        count += 1 
print(*number_lst)

# Подвиг 8.
n = int(input())
while n != 0: 
    for i in range(6, -1, -1):
        while n >= 2 ** i:
            n -= 2 ** i
            print(2 ** i, end=' ') 