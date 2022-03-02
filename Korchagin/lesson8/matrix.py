print("Введите размер матрицы")
n = int(input())

# A
A = []
for i in range(n):
    a = []
    for j in range(n):
        if i == j:
            a.append(1)
        else:
            a.append(0)
    A.append(a)

# B
B = []
for i in range(n):
    a = []
    for j in range(n):
        if j == n - i - 1:
            a.append(1)
        else:
            a.append(0)
    B.append(a)

print("Matrix A")
for item in A:
    print(item)

print("Matrix B")
for item in B:
    print(item)

sum = 0;
C = []
for i in range(n):
    c = []
    for j in range(n):
        for k in range(n):
            sum += A[i][k] * B[k][j]
        c.append(sum)
        sum = 0
    C.append(c)

print("\n\nMatrix C")
for item in C:
    print(item)