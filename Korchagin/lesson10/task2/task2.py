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
    len_xxx = find_max_len(text, char)

    for i in range(len_xxx, 1, -1):
        text = text.replace(char * i, f"{char}!{char}")
    return text


text = open("24_demo.txt", "r").read()
text_Y = open("24_demo.txt", "r").read()

text = replace_XXX(text, "X")
text = replace_XXX(text, "Y")
text = replace_XXX(text, "Z")

text_list = text.split("!")

count = 0
for item in text_list:
    if len(item) > count:
        count = len(item)

print(count)

print(find_max_len(text_Y, "Y"))


