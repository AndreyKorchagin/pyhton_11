# a = input()
string = "XYZxyz*"
print(string)
N = int(input())
list_numbers = []
test = ord("9")

for item in string:
    number = ord(item)
    if 65 <= number <= 90:
        new_number = number + N
        if new_number >= 90:
            new_number -= 26
    elif 97 <= number <= 122:
        new_number = number + N
        if new_number >= 122:
            new_number -= 26
    elif number == ord("*"):
        new_number = ord("9")

    list_numbers.append(chr(new_number))
print(list_numbers)
