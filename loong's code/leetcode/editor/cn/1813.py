import copy


class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        list1 = sentence1.split(' ')
        list2 = sentence2.split(' ')

        if len(list1) < len(list2):
            temp = list1
            list1 = list2
            list2 = temp
        ans=copy.deepcopy(list2)
        for i in list2:
            for index, j in enumerate(list1):
                if i == j and (index == 0 or index == len(list1) - 1):
                    ans.remove(i)
        if not ans:
            return True
        else:
            return False


print(Solution.areSentencesSimilar(Solution(), sentence1 ="Ogn WtWj HneS",sentence2 ="Ogn WtWj HneS"))


