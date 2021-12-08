string = "XYZ"
print(string)
# a = input()
N = int(input())
list_numbers = []

for item in string:
    new_number = ord(item) + N
    if new_number >= 90:
        new_number -= 26
    list_numbers.append(chr(new_number))
print(list_numbers)
