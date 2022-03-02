text = open("24.txt", "r").read()
text_list = text.split("A")
count = 0

for item in text_list:
    countE = 0
    for i in item:
        if i == "E":
            countE += 1
    if countE >= 3:
        if len(item) > count:
            count = len(item)

print(count)
