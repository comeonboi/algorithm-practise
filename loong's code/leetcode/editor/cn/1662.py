def arrayStringsAreEqual(word1: list[str], word2: list[str]) -> bool:
    return {True: True, False: False}["".join(word1) == "".join(word2)]


class Solution:
    word1 = ["ab", "c"]
    word2 = ["a", "bsc"]
    print(arrayStringsAreEqual(word1, word2))
