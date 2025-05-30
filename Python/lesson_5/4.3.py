# Подвиг 1.
a = float(input())
b = float(input())
d = a if a > b else b
print(d)

# Подвиг 2.
a = int(input())
result = "кратно 3" if a % 3 == 0 else "не кратно 3"
print(result)

# Подвиг 3.
word = input().lower()
msg = "палиндром" if word == word[::-1] else "не палиндром"
print(msg)

# Подвиг 4.
x = int(input())
msg = True if x else False
print(msg)

# Подвиг 5.
msg = int(input())
result = 0 if msg >= 59 else msg+1
print(result)

# Подвиг 6.
n = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']
a, b, c = map(int, input().split())
s1 = "#" + n[a-1] if a == 1 or a == 4 else n[a-1]
s2 = "#" + n[b-1] if b == 1 or b == 4 else n[b-1]
s3 = "#" + n[c-1] if c == 1 or c == 4 else n[c-1]
print(s1, s2, s3)