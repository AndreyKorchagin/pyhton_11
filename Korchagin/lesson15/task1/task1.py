text = open("24_demo.txt", "r").read()
count = 0
max = 0
for i in range(0, len(text)-1):
    if text[i] != text[i + 1]:
        count += 1
    else:
        if max < count:
            max = count
        count = 0
print(max)
