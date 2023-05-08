# Problem #5. Факториал
# Программа по вычислению факториала числа, заданного пользователем

n = int(input())
factorial = 1
for i in range(1, n + 1):
    print("factorial =", factorial, "*", i)
    factorial *= i
print("factorial =", factorial)