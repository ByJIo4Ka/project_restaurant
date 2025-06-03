# Подвиг 1.
list_number = [abs(float(num)) for num in input().split()]
print(list_number)

# Подвиг 2.
n = abs(int(input()))
print([int(x) for x in str(n)])

# Подвиг 3.
size_matrix = int(input())
matrix = [(1 if x == i else 0) for i in range(0, size_matrix) for x in range(0, size_matrix)]
count = 1
for i in matrix:
    if count % size_matrix == 0:
        print(i)
    else:
        print(i, end=" ")
    count += 1

# Подвиг 4. 
cites = input().split()
cites_5_symbols = [city for city in cites if len(city) > 5]
print(*cites_5_symbols)

# Подвиг 5. 
user_number = int(input())
list_number = [num for num in range(1, user_number+1) if user_number % num == 0]
print(*list_number)

# Подвиг 6.
size_matrix = int(input())
matrix_2 = [[x for i in range(size_matrix)] for x in range(size_matrix)]
for i in matrix_2:
    print(*i)

# Подвиг 7.
num_list = input().split()
num_index = [num_list[num] for num in range(0, len(num_list)) if float(num) % 2 == 0]
print(*num_index)

# Подвиг 8.
a, b = [map(int, input().split()) for _ in '12']
print(*map(sum, zip(a,b))) 

# Подвиг 9.
inp = input().split()                       
inp[1::2] = map(int, inp[1::2])
lst = list(map(list, zip(*[iter(inp)]*2)))
print(lst)