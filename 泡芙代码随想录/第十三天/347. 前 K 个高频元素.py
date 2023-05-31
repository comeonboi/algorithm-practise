class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        times = {}
        for i in range(len(nums)):
            if nums[i] not in times:
                times[nums[i]] = 1
            else:
                times[nums[i]] += 1
        tuple_list = list(times.items())
        tuple_list = sorted(tuple_list, key=lambda x: x[1], reverse=True)
        print(tuple_list)
        result = []
        for i in range(k):
            result.append(tuple_list[i][0])

        return result