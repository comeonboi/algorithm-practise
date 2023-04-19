def topKFrequent(nums: list[int], k: int) -> list[int]:
    list1 = {}
    list2 = []
    for i in nums:
        if i not in list1:
            list1[i] = 1
        else:
            list1[i] += 1
    maxNum = sorted(list1.values(), reverse=True)
    flag = 0
    for i in maxNum:

        if flag >= k:
            break
        flag += 1
        for j in list1:
            if list1[j] == i:
                if j not in list2:
                    list2.append(j)

    return list2


class Solution:
    print(topKFrequent(nums=[-1, -1], k=1))
