def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    intersection = set()
    nums1.sort()
    nums2.sort()
    for i in nums2:
        if i in nums1:
            intersection.add(i)
    return list(intersection)