print("Введите размер матрицы")
n = int(input())
m = int(input())

A = []
index = 1
for i in range(m):
    a = []
    for j in range(n):
        a.append(index)
        index += 1;
    A.append(a)

for item in A:
    print(item)

B = []
# B.append([]*4)
for i in range(n):
    b = []
    B.append(b)


for i in range(m):
    B.append([])
    for j in range(n):
        B[j].append(A[i][j])
# B[0][0] = 10
#

for item in B:
    print(item)