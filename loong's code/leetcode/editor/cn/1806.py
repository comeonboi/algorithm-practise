class Solution:
    def reinitializePermutation(self, n: int) -> int:
        perm = list(range(n))
        arr = [None] * n
        for i,index in enumerate(perm):
            if index % 2 == 0:
                arr[index] = perm[index//2]
            else:
                arr[index] = perm[n // 2 + (index - 1) // 2]
        print(arr)
        flag = 0
        for i in range(0, n):
            for j in range(i, n):
                if arr[i] > arr[j]:
                    temp = arr[i]
                    arr[i] = arr[j]
                    arr[j] = temp
                    flag+=1
        print(arr)
        return flag + 1

print(Solution.reinitializePermutation(Solution, n = 10))