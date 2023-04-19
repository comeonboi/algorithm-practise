class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        Str = ''
        List = []
        for i in word:
            if i.isdigit():
                Str += i
            else:
                if len(Str) > 0:
                    if int(Str) not in List:
                        List.append(int(Str))
                    Str = ''
        else:
            if len(Str) > 0:
                if int(Str) not in List:
                    List.append(int(Str))
        return len(List)


print(Solution.numDifferentIntegers(Solution, word="a1b01c001"))
