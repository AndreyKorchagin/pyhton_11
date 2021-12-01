a = input()
b = input()
lis = list(a)


print("Элементы списка после вставки  - это : ", end="")
for i in range(0, len(lis)):
    print(lis[i], end=" ")

print("\r")
lis.remove(b)
print("Элементы списка после удаления : ", end="")

for i in range(0, len(lis)):
    print(lis[i], end=" ")
print("Элементы списка после удаления : ", end="")
for i in range(0, len(lis)):
    print(lis[i], end=" ")
