# removing duplicate values from the list
lst = [10, 20, 10, 30, 20, 40, 50, 30]
new_lst = []

for i in lst:
    if i not in new_lst:
        new_lst.append(i)

print("List with duplicates removed:", new_lst)

