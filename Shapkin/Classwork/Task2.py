print("Введите числа")
a = int(input())
list_numbers = []

list_numbers.append(a)
while (a != 0):
    a = int(input())
    list_numbers.append(a)
list_numbers.remove(0)
sum = 0

for number in list_numbers:
    sum = sum + number
print(f"Сумма чисел = {sum}")
