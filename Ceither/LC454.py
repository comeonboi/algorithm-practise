import collections
def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
    # hash_table12 = {}
    # hash_table34 = {}
    # count = 0
    # n = len(nums1)
    # for i in range(n):
    #     for j in range(n):
    #         hash_table12[i, j] = nums1[i] + nums2[j]
    # for i in range(n):
    #     for j in range(n):
    #         hash_table34[i, j] = nums3[i] + nums4[j]
    # for i in hash_table12.values():
    #     for j in hash_table34.values():
    #         if i + j == 0:
    #             count += 1
    # return count
    c12 = collections.Counter(a + b for a in nums1 for b in nums2)
    return sum(c12[-c - d] for c in nums3 for d in nums4)