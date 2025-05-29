# Подвиг 2.
lst = list(map(int, input().split()))
lst.append(lst[0]!=lst[-1])
print(*lst)

# Подвиг 3.
cities = ["Москва", "Казань", "Ярославль"]
cities.insert(1, 'Ульяновск')
print(*cities)

# Подвиг 4.
lst = list(input())
lst.remove("+")
lst[0] = "8"
lst.remove("-")
lst.remove("-")
print("".join(lst))

# Подвиг 5.
s = (input().split())
print(f"{s[2]} {s[0][0]}.{s[1][0]}.")

# Подвиг 7.
lst = list(map(int, input().split()))
lst.sort()
print(*lst[:3])

# Подвиг 8.
lst = list(map(int, input().split()))
lst[-1] = lst[-1] % 2 != 0
print(*lst)

# Подвиг 9.
lst = list(map(int, input().split()))
print(lst.count(2))

# Подвиг 10.
lst = sorted(input().split())
lst.remove(lst[0])
print(*lst)