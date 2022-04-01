text = open("24_demo.txt", "r").read()
text = text.replace("XYZ", "*")
count = 0
max = 0
for i in range(len(text)):
    if text[i] == "*":
        count += 3
    else:
        if text[i] == "X":
            count != 0
            count += 1
        elif text[i] == "Y":
            count != 0
            count += 1
        if count > max:
            max = count
        count = 0
print(max)
