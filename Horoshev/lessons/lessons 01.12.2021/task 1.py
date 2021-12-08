string = "X"
new_world = []
for item in string:
    # print(ord(item)+4,end="")
    print(chr(ord(item) + 3), end="")
    new_world.append(chr(ord(item) + 3))
print(new_world)

new_str = "". join(new_world)
print(new_str)