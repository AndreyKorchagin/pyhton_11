string = "Hello world!"
for char in string:
    print(char)

for item in string:
    print(ord(item))

print(chr(40))

N = 10

new_world = []
for item in "Hello World":
    new_char = chr(ord(item) + N)
    print(new_char, end="")
    new_world.append(new_char)

print(f"new_world : {new_world}")

new_str = "".join(new_world)
print(new_str)
