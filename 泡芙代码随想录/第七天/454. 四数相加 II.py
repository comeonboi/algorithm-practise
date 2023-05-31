class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        two_dict = {}
        result = 0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if (nums1[i]+nums2[j]) not in two_dict:
                    two_dict[(nums1[i]+nums2[j])] =1
                else:
                    two_dict[(nums1[i]+nums2[j])] +=1
        for i in range(len(nums3)):
            for j in range(len(nums4)):
                if -(nums3[i] + nums4[j]) in two_dict:
                    result += two_dict[-(nums3[i] + nums4[j])]
        return result