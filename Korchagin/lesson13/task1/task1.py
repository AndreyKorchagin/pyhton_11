text = open("zadanie24_2 (1).txt", "r").read()

text = text.replace("LDR", "*")

print(4 % 3)

count = 0
max = 0
for item in text:
    if item == "*":
        count += 3
    elif item == "L" and count != 0:
        count += 1
    elif item == "D" and count % 3 == 1:
        count += 1
        if max < count:
            max = count
        count = 0
    else:
        if max < count:
            max = count
        count = 0

print(max)
