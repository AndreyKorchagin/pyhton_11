a = int(input())
list_numbers = []

list_numbers.append(a)
while (a != 0):
    a = int(input())
    list_numbers.append(a)

list_numbers.remove(0)
min = 1000
for number in list_numbers:

    if number < min:
        min = number
print(min)
