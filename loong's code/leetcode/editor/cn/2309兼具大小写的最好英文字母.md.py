class Solution:
    def greatestLetter(self, s: str) -> str:
        for i in range(90, 64, -1):
            if chr(i) in s and chr(i+32) in s:
                return chr(i)
        return ""

class Solution:
    def greatestLetter(self, s: str) -> str:
        # 我们可以用两个整数 mask1 和 mask2
        # 分别记录字符串 s 中出现的小写字母和大写字母，其中 mask1 的第 i 位表示第 i 个小写字母是否出现，
            # 而 mask2 的第 i 位表示第 i 个大写字母是否出现。
        mask1 = mask2 = 0
        for i in s:
            if i.islower():
                mask1 |= 1 << (ord(i) - ord("a"))
            else:
                mask2 |= 1 << (ord(i) - ord("A"))
        mask = mask1 & mask2
        return chr(mask.bit_length() - 1 + ord("A")) if mask else ""