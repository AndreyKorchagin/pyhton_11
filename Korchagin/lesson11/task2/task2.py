number_list = open("17 (1).txt", "r").read().split("\n")

count = 0
max = 0
for i in range(len(number_list) - 1):
    for j in range(i + 1, len(number_list)):
        if int(number_list[i]) * int(number_list[j]) % 14 != 0:
            count += 1
            sum = int(number_list[i]) + int(number_list[j])
            if sum > max:
                max = sum

print(f"count = {count}")
print(f"max = {max}")
