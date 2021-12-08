string = "XYZxyz"
new_world = []
for item in string:
    number = ord(item)
    if 65 <= number <= 90:
        new_number = number + 3
        if new_number >= 90:
            new_number = new_number - 26
            new_world.append(chr(new_number))
        else:
            new_world.append(chr(new_number))
    elif 97 <= number <= 122:
        new_number = number + 3
        if new_number >= 122:
            new_number = new_number - 26
            new_world.append(chr(new_number))
        else:
            new_world.append(chr(new_number))

print(new_world)

new_str = "".join(new_world)
print(new_str)
