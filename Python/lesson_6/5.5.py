# Подвиг 2
list_cites = list(input().split())
it = iter(list_cites)
print(next(it))
print(next(it))

# Подвиг 3
string_fir_iter = input()
it = iter(string_fir_iter)
flag = True
while flag:
    simbol = next(it)
    if simbol != ' ':
        print(simbol, end="")
    else:
        flag = False

# Подвиг 4
number = int(input())
string_number = str(number)
it = iter(string_number )
for i in range(0, int(len(string_number))):
    print(next(it), end=" ")