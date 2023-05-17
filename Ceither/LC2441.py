def findMaxK(self, nums: List[int]) -> int:
    # al = []
    # nums = list(set(nums))
    # for i in nums:
    #     if -i in nums:
    #         al.append(abs(i))
    # return max(al) if al else -1
    # hashtable
    hash_table = Counter(nums)
    li = []
    for key, value in hash_table.items():
        if key > 0 and -key in hash_table:
            li.append(key)
    return max(li) if li else -1