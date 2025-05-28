# Подвиг 2.

x = input()
print(x[0] + x[-1])
# Подвиг 5.

x = input()
print(x[:4])
# Подвиг 6.

x = input()
print(x[-3:])
# Подвиг 7.

x = input()
print(x[1::2])
# Подвиг 8.

x1 = input()
x2 = input()
print(x1[::2] + " " + x2[1::2])
# Подвиг 9.

x = input()
print(x[:5][::-1])
# Подвиг 10.

x1, x2 = input().split()
print(x2[:len(x1)])

# Подвиг 11.
x1, x2 = input().split()
print(x1[:len(x2)][1::2] == x2[1::2])