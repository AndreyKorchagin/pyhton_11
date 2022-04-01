text = open("zadanie24_1 (1).txt", "r").read()

count = 1
max = 0
for i in range(1, len(text)):
    if text[i] != text[i - 1]:
        count += 1
    else:
        if count > max:
            max = count
        count = 1

print(count)
print(max)
