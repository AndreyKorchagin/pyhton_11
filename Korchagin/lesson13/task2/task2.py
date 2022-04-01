text = open("zadanie24_2 (1).txt", "r").read()

text = text.replace("LDR", "*")

# print(4 % 3)

count = 0
max = 0
for item in text:
    if item == "L":
        count += 1
    else:
        if max < count:
            max = count
        count = 0

print(max)
