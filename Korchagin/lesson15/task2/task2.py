text = open("24_demo.txt", "r").read()
count = 0
maxim = 0
for i in range(0, len(text)):
    if text[i] == "X":
        count += 1
    else:
        maxim = max(count, maxim)
        count = 0
print(maxim)
