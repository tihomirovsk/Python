print('hello world')
colors = ['blue']

# типы данных и переменная
# int, float, boolean, str, list, None

# value = None

# a = 123
# b = 1.23
# print(type(a))
# print(type(b))
# value = 12334
# print(type(value))
# s = 'hello \nworld'

# print(s) # вывод строки

# print(a,'-', b,'-', s)
# print('{1} - {2} - {0}'.format(a, b, s))
# print(f'{a} - {b} - {s}')

# f = False
# print(f)

# list = ['1', '2', '3']
# col = ['hello', 1,2,4.5, True]
# print(list)
# print(col)

## print() - отвечает за вывод данных
## imput() - отвечает за ввод данных

### Ввод и вывод данных
# print, input

# print('Введите a');
# a = float(input())
# print('Введите b');
# b = float(input())
# print(a, ' + ', b, ' = ', a+b)
# print('{} {}'.format(a,b))
# print(f'{a} {b}')

### Арифметические операции
# +, -, *, /, %, //, **
# **,
# (), Сокращенные операции

# a = 1.312312
# b = 3
# c = round(a * b, 7)
# print(c)

# a = 3
# a *= 5
# print(a)


### Логические операции
# >, >=, <, <=, ==, !=
# not, and, or - не путать с &, |, ^
# is, is not, in, not in
# gen

# a = 1 < 3 < 5 < 10
# print(a)

# func = 1
# T = 4
# x = 123

# print(func<T>(x))

# f = 1 > 2 or 4 < 6

# print(f)

# f = [1,2,3,4]
# print(f)
# print(not 2 in f)

# is_odd = f[0] % 2 == 0
# print(is_odd)


### Управляющие конструкции
# if, if-else

# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print(a)
# else:
#     print(b)


# username = input('Введите имя: ')
# if username == 'Маша':
#  print('Ура, это же МАША!')
# elif username == 'Марина':
#  print('Я так ждала Вас, Марина!')
# elif username == 'Ильнар':
#  print('Ильнар - топ)')
# else:
#  print('Привет, ', username)

# original = 23
# inverted = 0
# while original != 0:
#  inverted = inverted * 10 + (original % 10)
#  original //= 10
# print(inverted)


# text = 'съешь ещё этих мягких французских булок'
# print(len(text)) # 39
# print('ещё' in text) # True
# print(text.isdigit()) # False
# print(text.islower()) # True
# print(text.repla

# text = 'съешь ещё этих мягких французских булок'
# print(text[0]) # c
# print(text[1]) # ъ
# print(text[len(text)-1]) # к
# print(text[-5]) # б
# print(text[:]) # print(text)
# print(text[:2]) # съ
# print(text[len(text)-2:]) # ок
# print(text[2:9]) # ешь ещё
# print(text[6:-18]) # ещё этих мягких
# print(text[0:len(text):6]) # сеикакл
# print(text[::6]) # сеикакл
# text = text[2:9] + text[-5] + text


### Cписок – пронумерованная, изменяемая коллекция объектов произвольных типов
# Списки: введение
# numbers = [1, 2, 3, 4, 5]
# print(numbers) # [1, 2, 3, 4, 5]
# numbers = list(range(1, 6))
# print(numbers) # [1, 2, 3, 4, 5]
# numbers[0] = 10
# print(numbers) # [10, 2, 3, 4, 5]
# for i in numbers:
#  i *= 2
#  print(i) # [20, 4, 6, 8, 10]
# print(numbers) # [10, 2, 3, 4,

### Списки: введение
# colors = ['red', 'green', 'blue']
# for e in colors:
#  print(e) # red green blue
# for e in colors:
#  print(e*2) # redred greengreen blueblue
# colors.append('gray') # добавить в конец
# print(colors == ['red', 'green', 'blue', 'gray']) # True
# colors.remove(


### Функции
# Это фрагмент программы, используемый многократно
# def function_name(x):
# body line 1
# . . .
# body line n
 # optional return

 # optional return

