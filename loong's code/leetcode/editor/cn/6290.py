from typing import List


class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        while k <= 0:
            # 假设把电站放在第一座，一直到最后一座
            for i in range(len(stations)):
                stations[i] += 1