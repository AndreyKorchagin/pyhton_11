print("Введите строку из которой нужно удалить:", end="")
a = input()
print("Введите символы которые нужно удалить:", end="")
b = input()
list_a = list(a)
list_b = list(b)

print("Элементы списка после вставки  - это : ", end="")
for i in range(0, len(list_a)):
    print(list_a[i], end=" ")

for item in list_b:
    list_b.remove(" ")

print()
for item in list_b:
    list_a.remove(item)
print(f"Элементы списка после удаления : {list_a}", end="")
