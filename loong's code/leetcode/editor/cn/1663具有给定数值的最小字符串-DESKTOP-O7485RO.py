class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        # 27 怎么拆解成 3 个数字 1 + 1 + 25
        # 73 怎么拆解成 5 个数字 1 + 1 + 19 + 26 + 26
        def find(list_ans):
            for i in range(n):
                while list_ans[i] < 26:
                    if sum(list_ans) == k:
                        return list_ans
                    list_ans[i] += 1
            return list_ans
        list1 = [1] * n
        list1 = ''.join(list(map(lambda x:chr(x) ,map(lambda x:x+96, find(list1)))))[::-1]
        return list1
#print(Solution.getSmallestString(Solution(),n =23100,k =567226))

class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        ans = ['a'] * n
        i, d = n - 1, k - n
        while d > 25:
            ans[i] = 'z'
            d -= 25
            i -= 1
        ans[i] = chr(ord(ans[i]) + d)
        return ''.join(ans)

print(Solution().getSmallestString(n = 23100, k = 567226))