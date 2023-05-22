def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    # if k == len(nums):
    #     return [max(nums)]
    # i, j = 0, k
    # ans = []
    # temp = nums[i:j]
    # while j < len(nums):
    #     ans.append(max(temp))
    #     temp.pop(0)
    #     temp.append(nums[j])
    #     i += 1
    #     j += 1
    # ans.append(max(temp))
    # return ans
    n = len(nums)
    q = [(-nums[i], i) for i in range(k)]
    heapq.heapify(q)

    ans = [-q[0][0]]
    for i in range(k, n):
        heapq.heappush(q, (-nums[i], i))
        while q[0][1] <= i - k:
            heapq.heappop(q)
        ans.append(-q[0][0])

    return ans