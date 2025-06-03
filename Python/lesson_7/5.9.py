# Подвиг 1.
import sys
s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]
[print(*x[::-1],end = ' ') for x in lst_in[::-1]]

# Подвиг 2.
list_in = list(map(int, input().split()))
size_matrix = int(len(list_in) ** 0.5)
result = [[list_in[size_matrix * i + j] for j in range(size_matrix)] for i in range(size_matrix)]
print(result)

# Подвиг 3.
list_in = ["– Скажи-ка, дядя, ведь не даром",
    "Я Python выучил с каналом",
    "Балакирев что раздавал?",
    "Ведь были ж заданья боевые,",
    "Да, говорят, еще какие!",
    "Недаром помнит вся Россия",
    "Как мы рубили их тогда!"
    ]
result = [[x for x in row.split() if len(x) > 3] for row in list_in]
print(result)

# Подвиг 4. 
import sys
s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]
result = [[row[i] for row in lst_in] for i in range(len(lst_in[0]))]
for row in result:
    print(*row)