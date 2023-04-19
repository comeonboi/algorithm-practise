from typing import List
# 天干地支
# 甲乙丙丁戊己庚辛壬癸
tiangan = ['geng', 'xin', 'ren', 'gui','jia', 'yi', 'bing', 'ding', 'wu', 'ji']
dizhi = ['zi', 'chou', 'yin', 'mao', 'chen', 'si', 'wu', 'wei', 'shen', 'you', 'xu', 'hai']
year = int(input())
# print(year)
n = (year - 2020) % 60
print(tiangan[n % 10] + dizhi[n % 12])

