print("Введите число N")
N = int(input())

print(f"N = {N}")

answer = 1
for i in range(1, N + 1):
    answer *= i

print(f"Answer = {answer}")
