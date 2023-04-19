from typing import List
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for _ in range(k):
            sqrt = max(gifts) ** 0.5
            gifts.remove(max(gifts))
            gifts.append(int(sqrt))
        return sum(gifts)
print(Solution.pickGifts(Solution,gifts = [25,64,9,4,100], k = 4))