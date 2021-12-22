list_a = [1, 2, 3, 4, 5, 5, 6, 7]
list_b = ["1", "2", "3", "4", "5", "5", "6", "7"]

list_all = []

list_all.append(list_a)
list_all.append(list_b)

print(list_all)
print(list_all[1])
print(list_all[1][6])

n = int(input())
m = int(input())

# n = 3
# m = 5
lst = []
for i in range(m):
    list_1 = []
    for j in range(n):
        if i == j:
            list_1.append("1")
        elif j == n - 1 - i:
            list_1.append("2")
        else:
            list_1.append("0")
    lst.append(list_1)

for item in lst:
    print(item)
