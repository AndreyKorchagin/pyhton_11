# a = input()
string = "XYZxyz"
print(string)
N = int(input())
list_numbers = []

for item in string:
    number = ord(item)
    # new_number = ord(item) + N
    if 65 <= number <= 90:
        new_number = number + N
        if new_number >= 90:
            new_number -= 26
        # list_numbers.append(chr(new_number))

    elif 97 <= number <= 122:
        new_number = number + N
        if new_number >= 122:
            new_number -= 26
    list_numbers.append(chr(new_number))
print(list_numbers)
