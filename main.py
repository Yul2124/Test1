#print("Hello World!")
#answer=input("Enter your name:")
#print(answer)
#print(5+5)
#n1 = int(input("Enter number1:"))
#n2 = int(input("Enter number2:"))
#print (f"Result:\n1. Summa:{n1+n2}\n2. Div: {n1 / n2}\n3. Mult: {n1 * n2}")
#num1 = int(input("Введіть num1:"))
#persent = int(input("Введіть persent:"))
#print(f"{persent}% від {num1} становить:{num1 * (persent/100)}")
#height=float(input("Enter height: "))
#width=
#num = int (input ("Enter a number:"))
#print (num //10)
#print (num%10)
#num = int (input ("Enter a number:"))
#n1 = num//100
#n2 = (num%100)//10
#n3 = num%10
#print(n1,"\n", n2, "\n", n1+n2+n3, sep="")
#n1 = int (input ("Enter a number1:"))
#n2 = int (input ("Enter a number2:"))
#print (int (n1+n2))
#n1 = int (input ("Enter a celsius:"))
#print(n1*9/5+32)
#Користувач вводить з клавіатури три числа. Розрахуйте суму чисел та добуток чисел. Результати обчислень
#виведіть на екран.
#n1 = int (input ("Enter a number1:"))
#n2 = int (input ("Enter a number2:"))
#n3 = int (input ("Enter a number3:"))
#print(n1+n2+n3, n1*n2*n3)
#Користувач вводить з клавіатури три числа. Перше
#число — зарплата за місяць, друге число — сума місячного
#платежу за кредитом банку, третє число — заборгованість
#за комунальні послуги. Виведіть на екран суму, яка залишиться у користувача після всіх виплат.
#n1 = int (input ("Enter salary:"))
#n2 = int (input ("Enter credit:"))
#n3 = int (input ("Enter communal:"))
#print (int (n1-n2-n3))
#Напишіть програму, яка підраховує площу ромба.
#Користувач вводить з клавіатури довжину двох його
#діагоналей.
#n1 = int (input ("Enter diagonal1:"))
#n2 = int (input ("Enter diagonal2:"))
#print (int (n1*n2)/2)
#num = int (input ("Enter a number:"))
#n1 = num//1000
#n2 = (num%1000)//100
#print (n1,n2)
#n3 = (num%100)//10
#print (n1,n2,n3)
#n4 = num%10
#n5 = n1+n4
#n6 = n2-n3
#n7 = n5*n6
#n8 = n7-(n1+n2+n3+n4)
#print(n8)
#
# ==, !=, <, >, <=, >=
# and or not
#age = input("Enter age: ")
#print ("Result", age>= 18 and age <= 150)
#num = 5
#print(num == 10 or num == 5)
#print(not 5==5)
# 0. () 1. not 2. and 3.or
# if умова:
#   умова вірна, виконується код який є на цьому рядку з відступами
# else:
# if умова:
# ....умова вірна виконується код який є на цьому рядку з відступами
# ....lkmskldfmkdkfl
# ....
# 22
# if 18 <= age <= 150:
#     print("Ви повнолітній! Ваша вікова категорія : ", end="")
#     if 30 <= age <= 70:
#         print("Дорослий")
#     else:
#         if 71 <= age <= 150:
#             print("Пенсіонер")
#         else:
#             print("Молодий")
# else:
#     print("Ви не повнолітній!")
# answer = input("Enter number: ")
# if answer == 'a':
#     print("Entered a")
# elif answer == 'b':
#     print("Entered b")
# elif answer == 'b':
#     print("Entered b")
# else:
#     print("Unknown")
#
# if answer == 'a':
#     print("Entered a")
# if answer == 'a':
#     print("Entered a")
# if answer == 'a':
#     print("Entered a")
# else:
#     print("Unknown")
# print("The end")
# 40
# num = int(input("Enter number: "))
# if num % 2 == 0:
#     print("2", end=" ")
# elif num % 3 == 0:
#     print("3", end=" ")
# elif num % 5 == 0:
#     print("5", end=" ")
# elif num % 10 == 0:
#     print("10", end=" ")

# Завдання 1
# Користувач вводить з клавіатури час у секундах, який
# минув з початку дня. Залежно від вибору користувача,
# підрахуйте, скільки годин, хвилин та секунд залишилося
# до півночі.
# sec = int(input("Enter seconds: ")) # 82800
# choose = input("What you want see(h/m/s):")
# seconds_in_day = 24 * 60 * 60
# if 0 <= sec <= seconds_in_day:
#     sec_left = seconds_in_day - sec
#     hours_left = sec_left // 3600
#     minutes_left = (sec_left % 3600) // 60
#     seconds_left = sec_left % 60
#     if choose == "h":
#         print("Hours left: ", hours_left)
#     elif choose == "m":
#         print("Minutes left: ", sec_left // 60)
#     elif choose == "s":
#         print("Seconds left: ", sec_left)
#     else:
#         print(f"Left: {hours_left}:{minutes_left}:{seconds_left}")
# else:
#     print("Incorrect value")
# Завдання 2
# Користувач вводить з клавіатури діаметр кола.
# Залежно від вибору користувача, підрахуйте площу або
# периметр кола.
# import math
# print(math.(4))
# diameter = float(input("Enter diameter: "))
# choice = input("P/S: ")
# if choice == "s":
#     print("Area: ", 3.14 * (diameter / 2) ** 2)
# elif choice == "p":
#     print("P: ", diameter * 3.14)
# Завдання 3
# Користувач вводить з клавіатури вартість однієї ігрової
# приставки, їх кількість та відсоток знижки. Залежно від
# вибору користувача, підрахуйте загальну суму замовлення
# або вартість однієї приставки з урахуванням знижки.
# price = int(input("Enter price of 1 products: "))
# quantity = int(input("Enter quantity of products: "))
# discount = int(input("Enter discount: "))
# choice = input("Enter choice(t/pd): ")
# if choice == 't':
#     print(f"Total amount: {quantity*price}")
# elif choice == 'pd':
#     print(f"Price one product with discount: {price*(1-discount/100)}")
# else:
#     print("Please select 't' or 'pd'")

# A B C
# import math
#
# A = int(input("Enter A: "))
# B = int(input("Enter B: "))
# C = int(input("Enter C: "))
# if A == 0:
#     A = 1
#
# D = B * B - 4 * A * C
#
# if D == 0:
#     x = -(B / (2 * A))
#     print("x1,2= ", x)
# elif D > 0:
#     x1 = (-B + math.sqrt(D)) / (2 * A)
#     x2 = (-B - math.sqrt(D)) / (2 * A)
#     print(f"x1: {x1}\nx2: {x2}")
# else:
#     print("Корнів нема!")

# Користувач вводить з клавіатури ціле шестизначне
# число. Напишіть програму, яка визначає, чи є введене
# число — щасливим (щасливим вважається шестизначне
# число, в якому сума перших трьох цифр дорівнює сумі
# других трьох цифр).
# Наприклад, 123321 — щасливе число, оскільки 1+2+3 =
# 3+2+1.
# З іншого боку, 378423 нещасливе число, оскільки
# 3+7+8 != 4+2+3.
# Якщо користувач ввів не шестизначне число, виведіть
# повідомлення про помилку
# x1 = int(input("Enter x1: "))
# # y1 = int(input("Enter y1: "))
# # if 0 < x1 > 8:
# #     print( "Значення параметру не є коректним" )
# # elif 0 < y1 > 8:
# #     print( "Значення параметру не є коректним" )
# # x2 = int(input("Enter x2: "))
# # y2 = int(input("Enter y2: "))
# # if 0 < x2 > 8:
# #     print( "Значення параметру не є коректним" )
# # elif 0 < y2> 8:
# #     print( "Значення параметру не є коректним" )
# # if x1 == x2 or y1 == y2
# #     print ("Yes")
# # else:
# #     print ("No")
# x1 = int(input("Enter x1: "))
# y1 = int(input("Enter y1: "))
# x2 = int(input("Enter x2: "))
# y2 = int(input("Enter y2: "))
# # if 0 < x2 > 8:
# #     print( "Значення параметру не є коректним" )
# # elif 0 < y2> 8:
# #     print( "Значення параметру не є коректним" )
#     if x1 == x2 or y1 == y2:
#         print("Yes")
#     else:
# #         print("No")
# x1=int(input("Enter x :"))
# y1=int(input("Enter y :"))
# x2=int(input("Enter x :"))
# y2=int(input("Enter y :"))
# if x1<x2 or y1==y2:
# print(f"x2{x2},y2{y2}")
# elif y1<y2 or x1==x2:
# print(f"x2{x2},y2{y2}")

# n1 = int(input("Enter number1:"))
# n2 = int(input("Enter number2:"))
# answer = input("Continue? (y/n ")
# if answer == "y":
#     continue
# else:
#     break
# print("The end")
# n = 5
# res = 1
# while n >= 1:
#     res *= n
#     n -= 1
# print(res)
# Користувач вводить з клавіатури два числа. Вкажіть
# усі числа у заданому діапазоні.
# n = 5
# n = 10
# while n<=m:
#     print(n, end =" ")
#     n += 1
#лавіатури два числа. Вкажіть усі
# непарні числа у заданому діапазоні. Якщо межі діапазону
# вказані неправильно, потрібно провести нормалізацію
# меж. Наприклад, користувач ввів 33 і 13. Потрібна нормалізація, після якої початок діапазону дорівнюватиме
# 13, а кінець дорівнюватиме 33.
# n = 5
# m = 10
# if n > m:
#     m, n = n,m
# while n<=m:
#     if n % 2 != 0:
#         print(n, end =" ")
#     n += 1
# Користувач вводить з клавіатури розмір сторони
# квадрата. Виведіть на екран заповнений квадрат. Розмір
# сторони дорівнює введеному розміру. Наприклад, якщо
# користувач ввів 3, на екрані буде виведено:
# ***
# ***
# ***
# n = 5
# i = 0
# while i < n:
#     print("*"*n)
#     i += 1

# n = 5
# i = 0
# while i < n:
#     j = 0
#     while j < n:
#         print("*", end = " ")
#         j += 1
#     print()
#     i += 1
# n = 10
# i = 0
# while i < n:
#     j = 0
#     while j < n:
#         print("*", end = " ")
#         j += 1
#     print()
#     i += 1

# line = "Hello"
# for i in line:
#     print("Hello")
# line = "Hello"
# for i in range (len (line) -1. -1, -1):
#     print(line)

# Завдання 1
# Користувач вводить число. Визначте кількість цифр у
# цьому числі, підрахуйте їх суму та середнє арифметичне.
# Визначте кількість нулів у цьому числі. Спілкування з
# користувачем реалізуйте через меню.
# n = int (input ("Enter number:"))
# digits_count = len(n)
# sum_of_digits = 0
# zero_count = 0
#
# for digit in n:
#     if digit == "0":
#         zero_count += 1
#     sum_digits += int (digit)
#
# if digit_count > 0^
#     avg = sum_of_digits/digits_count
# else:
#     avg = 0
#
# print(f"Count digits": {digits_count})
# Завдання 2
# Напишіть програму, яка виводить на екран шахівницю
# із заданим розміром клітинки. Наприклад, три:
# ***---***---***---***---
# ***---***---***---***---
# ***---***---***---***---
# ---***---***---***---***
# ---***---***---***---***
# ---***---***---***---***

# Завдання 3
# Напишіть програму, яка перевіряє користувача на
# знання таблиці множення. Програма виводить на екран
# два числа, користувач повинен ввести їх добуток. Розробіть
# кілька рівнів складності (відрізняються складністю
# та кількістю питань). Виведіть користувачеві оцінку
# його знань
# leg_a = float(input("Input first leg length: "))
# leg_b = float(input("Input second leg length: "))
# print("Hypotenuse length is " +
#  str((leg_a**2 + leg_b**2) ** .5))
 # потрібно вивести числа в діапазоні від 5 до 25 кратні 7
# for i in range(5, 25):
#     if i % 7 == 0:
#         print(i)
# import time
# start = time.time()
# time.sleep(5)
# end = time.time()
# print(end - start)

# number = 1
# while number <= 5:
#     print(number)
#     break
#     number += 1
# else:
#     print("I've counted from 1 to 5!")

# n = 10
# for i in range(n):
#     for j in range(n):
#         if i != 0 and j != 0 and n-1 != i and n-1 != j:
#             print("   ", end=" ")
#         else:
#             print(" * ", end=" ")
#     print()
# print(len(line))

# line = "Hello"
# print(line[::-1])
# for i in line[::-1]:
#     print(i, end="")
# for i in range(len(line) - 1, -1, -1):
#     print(line[i], end="")

# Завдання 1
# Користувач вводить число. Визначте кількість цифр у
# цьому числі, підрахуйте їх суму та середнє арифметичне.
# Визначте кількість нулів у цьому числі. Спілкування з
# користувачем реалізуйте через меню.
# 5602
# n = input("Enter number: ")
# digits_count = len(n)
# sum_of_digits = 0
# zero_count = 0
#
# for digit in n:
#     if digit == "0":
#         zero_count += 1
#     sum_of_digits += int(digit) # sub_of_digits = sub_of_digits + digit
#
# if digits_count > 0:
#     avg = sum_of_digits/digits_count
# else:
#     avg = 0
#
# print(f"Count digits: {digits_count}")
# print(f"Summa of digits: {sum_of_digits}")
# print(f"Average: {avg}")
# print(f"Zero count: {zero_count}")

# Завдання 2
# Напишіть програму, яка виводить на екран шахівницю
# із заданим розміром клітинки. Наприклад, три:
# ***---***---***---***---
# ***---***---***---***---
# ***---***---***---***---
# ---***---***---***---***
# ---***---***---***---***
# ---***---***---***---***
# size = 8
# rows = size * 8
# cols = size * 8
# for i in range(rows):
#     line = ""
#     for j in range(cols):
#         if (i // size) % 2 == (j // size) % 2:
#             line += "*"
#         else:
#             line += "-"
#     print(line)
# Завдання 3
# Напишіть програму, яка перевіряє користувача на
# знання таблиці множення. Програма виводить на екран
# два числа, користувач повинен ввести їх добуток. Розробіть
# кілька рівнів складності (відрізняються складністю
# та кількістю питань). Виведіть користувачеві оцінку
# його знань
# import random
#
# level = 5  # 1 2 5
# score = 0
#
# q = 5 + level * 5
# for i in range(q):
#     num1 = random.randint(1, 9)
#     num2 = random.randint(1, 9)
#
#     answer = int(input(f"Round #{i+1}\n{num1} * {num2} = ?\n>> "))
#     if answer == num1 * num2:
#         score += 1
#         print("Correct!")
#     else:
#         print(f"Incorrect! Correct answer is {num1 * num2}")
#
# print(f"Your score is {score}")


# "hello" -> 01010

# userMessage = 'Hello'
# userMessageEnc = userMessage.encode('utf-8')
# print(userMessageEnc)
# # 010101 -> "helo" # 0x021\0x0Ab\x012
# # 1010101
#
# userMessageDec = userMessageEnc.decode('utf-8')
# print(userMessageDec)


# myStr = "hello"
# x = "hello"
# print(id(myStr))
# print(type(myStr))
# print(myStr)
# x = """
#
#     Hello
#
# """
# print(x)
# -                  987653421
#       0123456789
# line = "305"
# 305
# 3+0+5
# print(int(line[0])+int(line[1])+int(line[2]))
# line = "Hello world"
# print(line)
# new_line = line.lower()
# print(new_line)
# print(line.upper())
# print(line.capitalize())
# print(line.title())
# print(line.swapcase())
# print(line)

# line = "Hello world"
# print(line)
# var = line.count('l', len(line) // 2, len(line))
# print(var)
# print(line.find('oijkb'))
# print(line.index('x'))
# print(line.rfind())
# print(line.rindex())

# line = "Hello world"
# print(line.startswith('l', 2, 5))
# print(line.endswith("l"))


# line = "!"
# print(line.isnumeric())
# print(line.isalpha())
# print(line.isdigit())
# print(line.istitle())
# print(line.isupper())
# print(line.isspace())
# print(line.isprintable())
# print(line.isidentifier())
# print(line.isdecimal())
# print(line.islower())
# print(line.isascii())
# print(line.isalnum())

# line = "   Hello world   "
#
# print(line.center(5, "*"))
# print(line.ljust(30, "*"))
# print(line.rjust(30, "*"))
# print(line.strip(' '))
# print(line.lstrip(' '))
# print(line.rstrip(' '))

# line = "Hello world"

# print(line[::-1])
# print(line[:5])
# print(line[5:])

# print(r"to create new line use - \n")
# name = "Alex"
# print(f"Name: {name}")
# mess_welcome = "Hello, {name}, {age}"
# name = "Alex"
# age = 20
# print(mess_welcome.format(name=name, age=age))
# mess_welcome = "Number is: {:.2f}"
#
# print(mess_welcome.format(5.1234567))
# myStr3 = "You have {:^10} points."
# print(myStr3.format(12))
# data = {'name': 'Alex', 'age': 2}
# text = "Hello {name} , my age {age}"
# print(text.format_map(data))
import string
import random

# pass_len = 8
# characters = string.ascii_letters + string.digits #+ string.punctuation
# password = ''.join(random.choice(characters) for i in range(pass_len)) # ('a', 5, 'b', '!', 1)
# #
# print(password)
# print('hello world'.replace('o', 'x').replace('l', '|'))

# import random
#
# userLogin = "".join(random.sample((string.ascii_lowercase), 6))
# userPass = "".join(random.sample((string.ascii_letters + string.digits), 8))
# print("login:", userLogin)
# print("password:", userPass)
# ._nkjnsa
# @
# gmail.com
# i.ua
# user@gmail.com
# import random
# ls = []
# for i in range(10):
#     ls.append(random.randint(-5, 10))
# print(ls)
# ls1 = [random.randint(-5,10) for i in range(10)]
# print(ls1)
# завдання
# у списку цілих, заповненому випадковими числами, розрахуйте:
# суму від’ємних чисел
# суму парних чисел
# суму непарних чисел
# добуток елементів, з індексами, кратними 3
# добуток елементів між мін та макс елементами
# суму елементів, що знаходяться між першим та останнім елементом
import random
ls = [random.randint(-5,10) for i in range(10)]
# s_neg = 0
# for i in ls:
#     if i < 0:
#         s_neg += i
# print("suma_negative =", s_neg)
# s_coup = 0
# for i in ls:
#     if i % 2 == 0:
#         s_coup += i
# print("suma_couples =", s_coup)
# s_odd = 0
# for i in ls:
#     if i % 2 != 0:
#         s_odd += i
# print("suma_odd =", s_odd)
# ind_3 = 1
# for i, item in enumerate(ls):
#     if i % 3 == 0:
#         ind_3 *= i
# print("ind_3 =", ind_3)
# добуток елементів між мін та макс елементами
# num_min_max = 1
# min_num = min(ls)
# max_num = max(ls)
# for num in ls:
#    if num > min_num and num < max_num:
#        num_min_max *= num
# print('num_min_max =', num_min_max)
# суму елементів, що знаходяться між першим та останнім елементом
# to do list
# tiile,  deskription, status, date
# import tabulate
# import time
# count = 1
# tasks = [{
#     'id': 1,
#     'title': 'asd',
#     'description': 'asd',
#     'status': "To do",
#     'created_date': time.strftime("%d %b %Y %H:%M", time.localtime())
# }]
#
# header = ['#', 'Title', 'Description', 'Status', 'Created Date']
#
# while True:
#     row_numbers = list(range(1, len(tasks) + 1))
#
#     print("\nTo do List!\n1. Add Task.\n2. Delete task.\n3. Edit task.\n4. Show tasks")
#     # CRUD - create read update delete
#     choose = input("Enter option: ")
#     if choose == "1":
#         count +=1
#
#         task = {
#             'id': count,
#             'title': input("Enter task name: "),
#             'description': input("Enter description: "),
#             'status': "To do",
#             'created_date': time.strftime("%d %b %Y %H:%M", time.localtime())
#         }
#         tasks.append(task)
#     elif choose == "2":
#         print()
#         rows = [x.values() for x in tasks]
#         print(tabulate.tabulate(rows, header))
#
#         choose = input("Enter number of task:")
#         del tasks[int(choose)-1]
#         print("Task Deleted!")
#     elif choose == "3":
#         print()
#         rows = [x.values() for x in tasks]
#         print(tabulate.tabulate(rows, header))
#
#         choose = int(input("Enter number of task to change:"))
#         task = tasks[choose - 1]
#         tasks[choose - 1] = {
#             'id': task['id'],
#             'title': input("Enter task new name: "),
#             'description': input("Enter new description: "),
#             'status': "To do",
#             'created_date': time.strftime("%d %b %Y %H:%M", time.localtime())
#         }
#     elif choose == "4":
#         print()
#         rows = [x.values() for x in tasks]
#         print(tabulate.tabulate(rows, header))
#     else:
#         print("Wrong option!")
#
# def print_mesagess():
#     print('Hello1')
#     print('Hello2')
#     print('Hello3')
#
# print_mesagess()


# name = 'Den'
# age = '20'
#
# def foo(name):#параметри
#     print('Hello' + name)
#
# foo('John')#aргумет


# Напишіть функцію, яка перевіряє чи є шестизначне число «щасливим».
# Число передається як параметр. Якщо число щасливе, поверніть з функції true, якщо ні — false.
# «Щасливе шестизначне число» — це число, в якому сума перших трьох цифр дорівнює сумі других трьох цифр.
# Наприклад, 123420 — щасливе 1+2+3 = 4+2+0, а 723422 — нещасливе 7+2+3 != 4+2+2.

# def is_lucky_number(number):
#     if not isinstance (number, int) or not 1000000 <=  number <= 99999:
#         return False
#     n_str = str(number)
#
#     sum_fist_three = sum(int(n_str[0]) for i in range (3))
#     sum_fist_three = sum(int(n_str[i]) for i in range(3, 6))
#
#     return sum_fist_three == sum_fist_three
#
# print(is_lucky_number(123321))
# print(is_lucky_number(123456))
# print(is_lucky_number(1))
# print(is_lucky_number("123"))




# Завдання 1
# Напишіть функцію, яка виводить на екран форматований текст, наведений нижче:
# “Don’t let the noise of others’ opinions
# drown out your own inner voice.”
# Steve Jobs
# def print_some():
#     some = "“Don’t let the noise of others’ opinions\n" \
#             "drown out your own inner voice.”\n" \
#             "Steve Jobs"
#     print(some)
#
# print_some()

# Завдання 2
# Напишіть функцію, яка приймає два числа як параметр і відображає усі непарні числа між ними.

# def непарні_числа (start, end):
#     if start > end:
#         start, end = end, start
#     for num in range(start+1, end):
#         if num % 2 != 0:
#             print(num)

# Завдання 4
# Напишіть функцію, яка повертає максимальне число
# із чотирьох. Числа передаються як параметри.

# def max_num (a, b, c, d, e, f):
#     return max(a, b, c, d, e, f)

# res = max_num (4,9,3,8,36,91)
# print(res)

# Завдання 5
# Напишіть функцію, яка повертає суму чисел у вказаному діапазоні. Межі діапазону передаються як параметри.
#
# def sum_num (start, end):
#     return sum(range(start, end+1))
# res = sum_num(1,5)
# print(res)

# Завдання 6
# Напишіть функцію, яка перевіряє чи є число простим.
# Число передається як параметр. Якщо число просте, поверніть з методу true, якщо ні — false.

# def prime_num (number):
#     for number in range(2, int(number ** 0.5) + 1):
#         if number > 1:
#             for i in range(2, number):
#                 if (number % i) == 0:
#                     return True
#         else:
#             return False
#
# print(prime_num(2))
# print(prime_num(3))
# def prime_num (number):
#     if number <= 1:
#         return False
#     for i in range(2, int (number**0.5) +1):
#         if number % i == 0:
#             return False
#     return True

# print(prime_num(2))
# print(prime_num(8))


# Задание 1
# Напишите функцию, вычисляющую сумму элементов
# списка целых. Список передаётся в качестве параметра.

# def sum_num (ls):
#        return sum(ls)
#
# ls = (4,5,9,4,6)
# print(sum_num(ls))

# Задание 2
# Напишите функцию для нахождения максимума в
# списке целых. Список передаётся в качестве параметра.

# def max_num (ls):
#     return max(ls)

# ls = (4,5,9,4,6)
# print(max_num(ls))

# Задание 3
# Напишите функцию, определяющую количество чётных, нечётных, положительных, отрицательных элементов
# списка целых. Список передаётся в качестве параметра.
# def some_num (ls):

# Задание 4
# Напишите функцию, переворачивающую содержимое
# списка целых.
# def rev_list (ls):
#     return ls [::-1]
#
# ls=(1, 2, 3, 4, 5)
# print(rev_list(ls))
# Задание 5
# Напишите функцию, которая ищет некоторое число
# в списке целых.
# Задание 6
# Напишите функцию, высчитывающую факториал
# каждого элемента списка целых. Функция возвращает
# новый список, содержащий полученные факториалы.

# def repeater ():
#     def wrapper (*args, **kwargs):
#         for _ in range (num_times):
#
# def foo ():
#     print("Hello")
#
#     Завдання
#     1
#     Напишіть
#     програму, яка
#     запитує
#     у
#     користувача
#     ім
#     'я та вік. Після отримання даних програма повинна виводити привітання у форматі: "Привіт, {ім'
#     я}! Твій
#     вік — {вік}
#     ". Обробіть виняток, що виникає при введенні некоректного віку (вік < 0 або вік > 130), і виведіть повідомлення про помилку.
# try:
#     name = input("Enter your name: ")
#     age = int(input("Enter your age:"))
#     if 0 > age or age > 100:
#         raise ValueError("Некоректний вік")
#     else:
#         print (f"Привіт {name}! Твій вік {age}")
# except ValueError as e:
#     print("Помилка:", e)
# Завдання 2
# Реалізуйте перше завдання через функцію. Функція повинна приймати ім'я і вік як параметри і повертати відформатований рядок. Перевірка коректності отриманих даних повинна бути всередині функції. Створіть дві версії реалізації функції:
# Перша версія не обробляє виняток всередині функції. Уся обробка знаходиться зовні;
# Друга версія обробляє виняток усередині функції.

# Дан текстовый файл. Необходимо создать новый файл, в который требуется
# переписать из исходного файла все слова, состоящие не менее чем из семи букв
# from string import ascii_letters, punctuation
#
# ascii_letters += "-"
# try:
#     infile = open("infile.txt", "r")
#     text = infile.read()
#     words = text.split()
#     long_words = [word.strip(punctuation) for word in words if len(word.strip(punctuation)) >= 7 and
#                   (word.replace('-', ' ').strip(punctuation).isalpha())]
#
#     outfile = open("outfile.txt", "w")
#     for word in long_words:
#         outfile.write(word + "\n")
#
# except Exception:
#     print("Error")
#
# else:
#     infile.close()
#     outfile.close()





# НОВЕ
# Задание 2 Дан текстовый файл. Необходимо переписать его строки в другой файл.
# Порядок строк во втором файле должен совпадать с порядком строк в заданном файле.

# try:
#     infile = open("infile.txt", "r")
#     text = infile.read()
#     words = text.split()
#
#     outfile = open("outfile.txt", "w")
#     for word in words:
#         outfile.write(word + " ")
#
# except Exception:
#     print("Error")
#
# else:
#     infile.close()
#     outfile.close()
# #
# Задание 3 Дан текстовый файл. Необходимо переписать его строки в другой файл.
# Порядок строк во втором файле должен быть обратным по отношению к порядку строк в заданном файле.

# try:
#     infile = open("infile.txt", "r")
#     lines = infile.readlines()
#
#     outfile = open("outfile.txt", "w")
#     for line in reversed(lines):
#         outfile.write(line + "\n" )
#
# except Exception:
#     print("Error")
#
# else:
#     infile.close()
#     outfile.close()

# Задание 4 Дан текстовый файл. Добавить в него строку из двенадцати звездочек (************),
# поместив ее после последней из строк, в которых нет запятой. Если таких строк нет,
# то новая строка должна быть добавлена после всех строк имеющегося файла.
# Результат записать в другой файл.

try:
    infile = open("infile.txt", "r")
    lines = infile.readlines()

    last_ind = -1
    for i in range(len(lines)):
        if ',' not in lines[i]:
            last_ind = i

    if last_ind == -1:
        lines.append("************\n")
    else:
        lines.insert(last_ind + 1, "************\n")

    outfile = open("outfile.txt", "w")
    outfile.writelines(lines)
    outfile.flush()

except Exception as e:
    print("Error:", e)

else:
    infile.close()
    outfile.close()

# Дан текстовый файл.
# Переписать в другой файл все его строки с заменой
# в них символа * на символ & и наоборот.

# try:
#     infile = open("infile.txt", "r")
#     lines = infile.readlines()
#
#     new_lines = []
#
#     for line in lines:
#         new_line = line.replace('*', '&').replace('&', '*')
#         new_lines.append(new_line)
#
#     outfile = open("outfile.txt", "w")
#     outfile.writelines(new_lines)
#     outfile.flush()
#
# except Exception as e:
#     print("Error:", e)
#
# else:
#     infile.close()
#     outfile.close()

# import csv
#
# data = [
#     ["Name", "Age", "City"],
#     ["Den", "20", "Lviv"],
#     ["Leya", "30", "New York"]
# ]
#
# with open("output.csv", "w", newline="") as f:
#     writer = csv.writer(f)
#     writer.writerows(data)
#
# with open("output.csv", "r", newline="") as f:
#     reader = csv.reader(f)
#     header = next(reader)
#     for row in reader:
#         print(row)

# import csv
#
# data = [
#     {"Name": "Den", "Age": "25", "City": "Lviv"},
#     {"Name": "Ben", "Age": "35", "City": "Boston"},
#     {"Name": "Don", "Age": "55", "City": "London"},
# ]
# fieldnames = ['Name', 'Age', 'City']
#
# with open("output.csv", "w", newline="") as f:
#     writer =csv.DictWriter(f, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerows(data)
#
#
# with open("output.csv", "r", newline="") as f:
#     reader = csv.reader(f)
#     header = next(reader)
#     for row in reader:
#         print(row)

# import os
#
# # os.mkdir('new')#add
# # os.rmdir('new') #delete
# # os.remove('new/file.txt')#remove file from
# # os.rename('outfile.txt', 'new_outfile.txt')#перезаписать
#
# # print(os.getcwd())
#
# path = input('Enter path to directory: ')
#
# def list_dir (path, level=0):
#     try:
#         items = os.listdir(path)
#     except PermissionError:
#         return
#     for item in items:
#         item_path = os.path.join(path, item)
#         print('    '*level+'|--'+item)
#         if os.path.isdir(item_path):
#             list_dir(item_path, level+1)
#
# if os.path.exists(path) and os.path.isdir(path):
#     print("Contain directory: ")
#     list_dir(path)
# else:
#     print("Incorrect path!")
print('Hello')
