lst = [1, 2, 3, 4, 5, 6]
v = 3

print(lst.index(v))

for i, value in enumerate(lst):
    if value == v:
        print(i)
        break

for i in range(len(lst)):
    if lst[i] == v:
        print(i)
        break

