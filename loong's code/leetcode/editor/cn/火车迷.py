from typing import List
T = int(input())
for _ in range(T):
    n = int(input())
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))
    # print(n, x_list, y_list)
    ans = []
    # i 为入栈个数
    for i in range(len(x_list)):
        if y_list == x_list[i:] + (x_list[:i][::-1]):
            print('Yes')
            break
        # print(ans)
    else:
        print("No")

all_list = []
while 1:
    aaa = input()
    if aaa != "":
        all_list.append(aaa)
    else:
        break
times = int(all_list[0])
i = 1
data_list = []
while i < len(all_list):
    temp_object = []
    num = int(all_list[i])
    i += 1
    list1 = all_list[i].split(" ")
    for j in range(len(list1)):
        list1[j] = int(list1[j])
    i += 1
    reversed_list = all_list[i].split(" ")
    for j in range(len(reversed_list)):
        reversed_list[j] = int(reversed_list[j])
    i += 1
    temp_object.append(num)
    temp_object.append(list1)
    temp_object.append(reversed_list)
    data_list.append(temp_object)


def solution(num1, list, reversed_list):
    if len(list) != num1:
        return "No"
    index1 = 0
    index2 = 0
    stack = []
    while index1 != len(list):
        stack.append(list[index1])
        index1 += 1
        while len(stack) != 0 and stack[-1] == reversed_list[index2]:
            stack = stack[:-1]
            index2 += 1
    while index2 != len(reversed_list):
        if stack[-1] == reversed_list[index2]:
            stack = stack[:-1]
            index2 += 1
        else:
            index2 += 1
    if len(stack) > 0:
        return "No"
    else:
        return "Yes"


for i in range(times):
    print(solution(data_list[i][0], data_list[i][1], data_list[i][2]))
