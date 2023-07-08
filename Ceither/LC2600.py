class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        if k <= numOnes:
            return k
        if numOnes < k <= numOnes + numZeros:
            return numOnes
        if numOnes + numZeros < k <= numOnes + numZeros + numNegOnes:
            return numOnes - (k - (numOnes + numZeros))