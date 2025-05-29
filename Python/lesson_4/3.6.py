# Подвиг 3.
lst = list(map(int, input().split()))
print(lst)

# Подвиг 4.
cities = input().split()
print("Москва" in cities)

# Подвиг 6.
cities = input().split()
print(cities[-1])

# Подвиг 7.
marks = list(map(int, input().split()))
print(round(sum(marks) / len(marks), 1))

# Подвиг 8.
name_book = input()
name_author = input()
pages = int(input())
price = float(input())
book = [name_book, name_author, pages, price]
del book[2]
book[1] = "Пушкин"
book[2] = book[2] * 2
print(book)

# Подвиг 9.
lst = list(map(int, input().split()))
print(max(lst), min(lst), sum(lst))

# Подвиг 10.
lst = list(map(int, input().split()))
print(*sorted(lst, reverse = True))

# Подвиг 12.
cities = ["Москва", "Тверь", "Вологда"]
lst = cities + input().split()
print(*lst)

# Подвиг 13.
cities = ["Москва", "Тверь", "Вологда"]
lst = input().split() + cities
print(*lst)