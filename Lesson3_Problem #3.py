#Problem #3. Беги, герой!
#Вася начал бегать и в первый день он пробежал X километров и выдохся.
#Вася поставил себе цель Y километров и решил узнать, когда он ее достигнет,
#если каждый день будет бегать дистанцию на 10% больше, чем в предыдущий.

#ФОРМАТ ВВОДА
#Программа получает на вход целые числа X, Y
#ФОРМАТ ВЫВОДА
#Одно целое число (день, когда Вася пробежит свою цель)

#Пример
#Ввод
#10 21
#Вывод
#9

# Specify the mileage on the first day and our goal
x, y = int(input()), int(input())

# Count the number of days
day = 1

while x <= y:
    x = x + (x * 0.1)
    day += 1

print(day)

# Solutions from the Internet
#x = int(input())
#y = int(input())
#day = 1
#while y - x > 0:
    #x = x + (x * 0.1)
    #day += 1
#print(day)

#x = int(input())
#y = int(input())
#i = 1
#while x < y:
    #x *= 1.1
    #i += 1
#print(i)