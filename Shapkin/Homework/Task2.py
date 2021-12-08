print("Введите чилса А и Б, где A < Б")
print("Введите число А")
A = int(input())
print("Введите число Б")
B = int(input())

print(f"A = {A}; B = {B}")

i = A
while(i <= B):
    if i % 3 == 0:
        print(i)
    i += 1
