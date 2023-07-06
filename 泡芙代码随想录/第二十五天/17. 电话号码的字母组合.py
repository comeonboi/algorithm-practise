class Solution:
    def __init__(self):
        self.letterMap = [
            "",  # 0
            "",  # 1
            "abc",  # 2
            "def",  # 3
            "ghi",  # 4
            "jkl",  # 5
            "mno",  # 6
            "pqrs",  # 7
            "tuv",  # 8
            "wxyz"  # 9
        ]
        self.result = []
        self.s = ""

    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return self.result
        self.back_tracking(digits, 0)
        return self.result

    def back_tracking(self, digits, start_num):
        if len(self.s) == len(digits):
            self.result.append(self.s)
            return
        digit = int(digits[start_num])
        letters = self.letterMap[digit]
        for i in range(len(letters)):
            self.s += letters[i]
            self.back_tracking(digits, start_num + 1)
            self.s = self.s[:-1]
