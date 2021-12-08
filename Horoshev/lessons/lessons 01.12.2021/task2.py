string = "HELLOYZ"
new_world = []
for item in string:
    number = ord(item)
    new_number = number + 3
    if new_number >= 90:
        new_number = new_number - 25
        new_world.append(chr(new_number))
    else:
        # new_number <= 90
        # new_number = new_number + 3
        new_world.append(chr(new_number))

# print(ord(item) + 3, end="")
# print(chr(ord(item) + 3), end="")
# new_world.append(chr(ord(item) + 3))
print(new_world)

new_str = "".join(new_world)
print(new_str)
