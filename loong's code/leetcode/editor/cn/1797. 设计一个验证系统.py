from collections import defaultdict
from typing import List


class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive
        self.d = defaultdict(int)

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.d[tokenId] = currentTime + self.timeToLive

    def renew(self, tokenId: str, currentTime: int) -> None:
        if self.d[tokenId] <= currentTime:
            return
        self.d[tokenId] = currentTime + self.timeToLive

    def countUnexpiredTokens(self, currentTime: int) -> int:
        count = 0
        for j in self.d.values():
            if currentTime < j:
                count += 1
        return count


# Your AuthenticationManager object will be instantiated and called as such:

print(obj := AuthenticationManager(5))
print(obj.renew("aaa", 1))
print(obj.generate("aaa", 2))
print(param_3 := obj.countUnexpiredTokens(6))
