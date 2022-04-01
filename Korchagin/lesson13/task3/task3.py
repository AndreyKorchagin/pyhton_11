text = open("24.txt", "r").read()

# print(text)

# for item in text

# print(len(text))
# print(text[100])
# print(text[101])
# print(text[102])
#                 1; N-1
count = 0
lst = []
for i in range(1, len(text) - 1):
    if text[i - 1] == text[i + 1]:
        count += 1
        lst.append("%s%s%s" % (text[i - 1], text[i], text[i + 1]))

dicct = {}

# dicct["A"] = 1

# print(dicct)
# print(dicct["A"])
# print(dicct.get("B"))

for item in lst:
    # print("%s -> %s" % (item, item[1]))
    string = item[1]
    if dicct.get(string) == None:
        dicct[string] = 1
    else:
        count = dicct.get(string)
        dicct[string] = count + 1

# print(dicct)

maxCount = 0
maxLetter = ""

for item in dicct:
    # print(item)
    if dicct.get(item) > maxCount:
        maxCount = dicct.get(item)
        maxLetter = item

print(maxLetter)