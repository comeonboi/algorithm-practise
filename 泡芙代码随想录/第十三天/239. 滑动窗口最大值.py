class Solution:
    def __init__(self):
        self.queue = []
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        for i in range(k):
            self.push(nums[i])
        result = []
        result.append(self.front())
        for i in range(k,len(nums)):
            self.pop(nums[i-k])
            self.push(nums[i])
            result.append(self.front())
        return result

    def pop(self,value):
        if self.queue and value == self.queue[0]:
            self.queue = self.queue[1:]
    def push(self,value):
        while self.queue and self.queue[-1] < value:
            self.queue.pop()
        self.queue.append(value)

    def front(self):
        return self.queue[0]
