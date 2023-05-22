import collections
def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    return heapq.nlargest(k, collections.Counter(nums).keys(), key=collections.Counter(nums).get)