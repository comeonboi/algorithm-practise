from typing import List


class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        time = 0
        for i in range(len(energy)):
            if initialEnergy <= energy[i]:
                time += energy[i] - initialEnergy + 1
                initialEnergy += energy[i] - initialEnergy + 1
            if initialExperience <= experience[i]:
                time += experience[i] - initialExperience + 1
                initialExperience += experience[i] - initialExperience + 1
            # initialEnergy > energy[i] and initialExperience > experience[i]:
            initialExperience += experience[i]
            initialEnergy -= energy[i]

        return time

print(Solution.minNumberOfHours(Solution(),initialEnergy = 5, initialExperience = 3, energy = [1,4,3,2], experience = [2,6,3,1]))