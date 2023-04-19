from typing import List


class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        # 精度未小数点后五位
        fahrenheit: float = celsius * 9 / 5 + 32
        kelvin: float = celsius + 273.15
        return [round(kelvin, 5),round(fahrenheit, 5)]


print(Solution.convertTemperature(Solution(), 36.5))
