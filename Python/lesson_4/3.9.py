# Подвиг 1.
a = [5.4, 6.7, 10.4]
x = list(map(int, input().split()))
a.append(x)
print(a)

# Подвиг 2.
lst = []
lst.append(input().split())
lst.append(input().split())
lst.append(input().split())
print(lst)

# Подвиг 3.
x1 = list(map(int, input().split()))
x2 = list(map(int, input().split()))
x3 = list(map(int, input().split()))
print(x1[-1], x2[-1], x3[-1])

# Подвиг 6.
t = [["Скажи-ка", "дядя", "ведь", "не", "даром"],
    ["Я", "Python", "выучил", "с", "каналом"],
    ["Балакирев", "что", "раздавал?"]]
w = input()
print(w in t[0] or w in t[1] or w in t[2])