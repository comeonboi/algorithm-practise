class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        x = 0
        for i in operations:
            if i == "--X" or i == "X--":
                x -= 1
            else:
                x += 1
        return x

print(Solution.finalValueAfterOperations(Solution(), operations=["--X", "X++", "X++"]))
