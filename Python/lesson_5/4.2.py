# подвиг 1.
m = int(input())
if m == 1:
    print("1. Введение в Python")
if m == 2:
    print("2. Строки и списки")   
if m == 3:
    print("3. Условные операторы")
if m == 4:
    print("4. Циклы")
if m == 5:
    print("5. Словари, кортежи и множества")
if m == 6:
    print("6. Выход")

# Подвиг 2.
a, b, c = map(int, input().split())
if a < b:
    if a < c:
        print(a)
    else:
        print(c)
elif b < c:
    print (b)
else:
    print(c)

# Подвиг 3.
x = float(input())
if x <= 60:
    print(1)
elif x <= 64:
    print(2)
elif x <= 69:
    print(3)
elif x > 69:
    print(4)

# Подвиг 4.
x = int(input())
if x == 1:
    print('понедельник')
elif x == 2:
    print('вторник')
elif x == 3:
    print('среда')
elif x == 4:
    print('четверг')
elif x == 5:
    print('пятница')
elif x == 6:
    print('суббота')
elif x == 7:
    print('воскресенье')

# Подвиг 5.
number_mounth = int(input())
if number_mounth == 1:
    print('31')
elif number_mounth == 2:
    print('28')
elif number_mounth == 3:
    print('31')
elif number_mounth == 4:
    print('30')
elif number_mounth == 5:
    print('31')
elif number_mounth == 6:
    print('30')
elif number_mounth == 7:
    print('31')
elif number_mounth == 8:
    print('31')
elif number_mounth == 9:
    print('30')
elif number_mounth == 10:
    print('31')
elif number_mounth == 11:
    print('30')
elif number_mounth == 12:
    print('31')

# Подвиг 6.
m, n=map(int,input().split())
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if 1<=m<13:
    if 1<n<days[m-1]:
        n_1=n-1
        m_1=m
        n_2=n + 1
        m_2=m
    elif n==1:
        n_1=days[m-1-1]
        m_1=m-1
        n_2=n+1
        m_2=m
    elif n==days[m-1]:
        n_1=n-1
        m_1=m
        n_2=1
        m_2=m+1
print(f"{str(m_1).rjust(2,'0')}.{str(n_1).rjust(2,'0')} {str(m_2).rjust(2,'0')}.{str(n_2).rjust(2,'0')}")

# Подвиг 7.
a = int(input())
if a % 7 == 1:
    print('понедельник')
elif a % 7 == 2:
    print('вторник')
elif a % 7 == 3:
    print('среда')
elif a % 7 == 4:
    print('четверг')
elif a % 7 == 5:
    print('пятница')
elif a % 7 == 6:
    print('суббота')
elif a % 7 == 7:
    print('воскресенье')