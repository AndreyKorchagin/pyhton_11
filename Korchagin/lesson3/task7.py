# Пользователь вводит число N. Выведите N-ное по счету число Фибоначчи.
# Последовательность чисел Фибоначчи рассчитывается
# по такой формуле: F(1) = 1, F(2) = 1, F(K) = F(K-2) + F(K-1).
# Идея такая: каждое следующее число равно сумму двух предыдущих.
#
# Первые 10 чисел последовательности: 1 1 2 3 5 8 13 21 34 55 ...

print("Введите число N")
N = int(input())

print(f"N = {N}")

F = [1, 1]

for i in range(2, N + 1):
    F.append(F[i - 1] + F[i - 2])

print(F[N - 1])