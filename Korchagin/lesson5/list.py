i = 1


def print_index():
    global i
    print(f"\n#{i}")
    i += 1


print_index()
lst = []  # Пустой список
print(lst)

print_index()
lst = [1, 2, 3, 4, 5]
print(lst)  # Заполненный список

print_index()
lst = ["Hello", "Worls", "My", "Apple"]
print(lst)

print_index()
lst = [1.5, 4.34, 55.66]
print(lst)

print_index()
lst = ["Hello", 5, "Father", 5.45]
print(lst)

print_index()
lst = [4 + 5, 5 + 8]
print(lst)

print_index()
lst = [1, 3, 4, 5, [1, 2, 3, ["a", "b", "c"]]]
print(lst)
print(lst[1])
print(lst[4])
print(lst[4][0])
print(lst[4][3][1])

print_index()
lst = [1, 2, 3, 4, 5]
print(lst[-1])
print(lst[-2])

print_index()
string = "Hello world"
lst = list(string)
print(lst)
print(lst[2])

print_index()
lst = list(range(10))
print(lst)

print_index()
lst = list(range(2, 10))
print(lst)

print_index()
lst = list(range(2, 10, 2))
print(lst)

print_index()
lst = [1, 2, 3, "c", 5, 4, "a"]
print(len(lst))

print_index()
print(len("Hello world !"))

print_index()
lst = [1, 2, 3, "c", 5, 4, "a"]
print(lst[3:6])

print_index()
lst = [1, 2, 3, "c", 5, 4, "a"]
print(lst[3:])

print_index()
lst = [1, 2, 3, "c", 5, 4, "a"]
print(lst[3:7:2])

print_index()
lst = [1, 2, 3, "c", 5, 4, "a"]
print(lst[::2])

print_index()
lst = [1, 2, 3, "c", 5, 4, "a"]
lst.append("Hello")
print(lst)

print_index()
lst = [1, 2, 3, "c", 5, 4, "a"]
lst.append(list("Hello"))
print(lst)
print(lst)

print_index()
lst = [1, 2, 3, "c", 5, 4, "a"]
lst.insert(3, "TEST")
print(lst)

print_index()
lst = [1, 2, 3, "c", 5, 4, "a"]
lst.pop(3)
print(lst)

print_index()
lst = [1, 2, 3, "c", 5, 4, "a"]
lst.pop()
print(lst)

print_index()
lst = [1, 2, 3, "c", 5, 4, "a"]
lst.pop()
print(lst)

print_index()
lst = [1, 2, 3, "c", 3, 5, 4, "a"]
lst.remove(3)
print(lst)

print_index()
lst = [5, 6, 7, 8, 1, 2, 3, 4]
lst.sort()
print(lst)

print_index()
lst = [5, 6, 7, 8, 1, 2, 3, 4]
lst.sort(reverse=True)
print(lst)

print_index()
lst = [1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 4, 5]
print(lst.count(1))
print(lst.count(2))
print(lst.count(3))
print(lst.count(4))
print(lst.count(5))

print_index()
lst = [1, 2, 3, 4]
new_lst = lst
print(f"lst = {lst}")
print(f"new_lst = {new_lst}")
new_lst.pop()
print()
print(f"lst = {lst}")
print(f"new_lst = {new_lst}")

print_index()
lst = [1, 2, 3, 4]
new_lst = lst.copy()
print(f"lst = {lst}")
print(f"new_lst = {new_lst}")
new_lst.pop()
print()
print(f"lst = {lst}")
print(f"new_lst = {new_lst}")

print_index()
lst = [4, 3, 2, 5, 6, 7, 1]
print(lst)
lst.reverse()
print(lst)

print_index()
lst = [1, 2, 3, 4, 5, 6]
new_lst = list("Hello world")
print(f"before lst = {lst}")
print(f"before new_lst = {new_lst}")
lst.extend(new_lst)
print()
print(f"after lst = {lst}")
print(f"after new_lst = {new_lst}")

print_index()
lst = [1, 2, 3, 4]
lst.clear()
print(lst)

print_index()
lst = [1, 2, 3, 4, 5]
print(lst.index(2))

print_index()
lst = [1, 2, 3, 4, 5, 6]
for j in range(len(lst)):
    print(lst[j])

print_index()
print_index()
lst = [1, 2, 3, 4, 5, 6]
for item in lst:
    print(item)
