class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        list1 = s
        length = len(str(k))
        start = 0
        tail = start + length
        ans = []
        while list1:
            while int(list1[start:tail]) > k:
                tail -= 1
                if tail == 0:
                    return -1
                if int(list1[start:tail]) <= k:
                    ans.append(list1[start:tail])
                    list1 = list1[:start]+list1[tail:]
                    tail = length
                    break

            if int(list1[start:tail]) <= k:
                ans.append(list1[start:tail])
                list1 = list1[:start]+list1[tail:]
        return len(ans)


print(Solution.minimumPartition(Solution(), s =
"1829727651",
k =
10))