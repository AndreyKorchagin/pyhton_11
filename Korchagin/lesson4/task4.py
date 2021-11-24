# Пользователь вводит числа до тех пор, пока не введет 0.
# Выведите максимальное введенное число (0 считать не нужно).

a = int(input())
list_numbers = []

list_numbers.append(a)

while (a != 0):
    a = int(input())
    list_numbers.append(a)
list_numbers.remove(0)

print("Вы ввели следующие числа:")
print(list_numbers)

print(f"Количество элементов в списке = {len(list_numbers)}")

# Пример без использования без индексов к списку
max = -1000
for number in list_numbers:
    if number > max:
        max = number

print(f"Максимальное число = {max}")

# Пример с использования индексов к списку
max1 = -1000
for i in range(len(list_numbers)):
    if list_numbers[i] > max1:
        max1 = list_numbers[i]

print(f"Максимальное число = {max1}")
