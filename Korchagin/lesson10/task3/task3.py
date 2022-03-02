def find_max_len(text, simbol):
    count = 0
    max = 0
    for i in text:
        if i == simbol:
            count += 1
        else:
            if max < count:
                max = count
            count = 0
    return max

def replace_XXX(text, char):
    text = text.replace("XYZ", "!");
    text = text.replace("XY", "#");
    text = text.replace("X", "$");
    return text

text = open("24_demo.txt", "r").read()

text = replace_XXX(text, "X")
print(text)

length = find_max_len(text, "!")
if text.find("!"*length+"#") != -1:
    print(length * 3 + 2)
elif text.find("!"*length+"$") != -1:
    print(length * 3 + 1)
else:
    print(length * 3)