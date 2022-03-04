text_list = open("17 (1).txt", "r").read().split("\n")

count = 0
max = 0
print(f"len = {len(text_list)}")

for i in range(len(text_list) - 1):
    if int(text_list[i]) % 3 == 0 or int(text_list[i + 1]) % 3 == 0:
        sum = int(text_list[i]) + int(text_list[i + 1])
        if sum > max:
            max = sum
        count += 1

print(f"count = {count}")
print(f"max = {max}")
