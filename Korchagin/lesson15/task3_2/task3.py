text = open("24_demo.txt", "r").read()
text = text.replace("XYZ", "*")
count = 0
max = 0
for item in text:
    if item == "*":
        count += 3
    elif item == "X"and count % 3 == 0:
        count += 1
    elif item == "Y" and count % 3 == 1:
        count += 1
        if max < count:
            max = count
        count = 0
    else:
        if max < count:
            max = count
        count = 0
print(max)
