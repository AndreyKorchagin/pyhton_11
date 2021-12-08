print("Введите число N")
N = int(input())

print(f"N = {N}")

F = [1, 1]

for i in range(2, N + 1):
    F.append(F[i - 1] + F[i - 2])

print(F[N - 1])