list1 = input().split(' ')
list2 = []
for i in list1:
    if i.isdigit():
        list2.append(int(i))
if set(list2) == 1:
    print(-1)
print(sorted(list2)[-2])