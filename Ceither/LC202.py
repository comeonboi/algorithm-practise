def isHappy(self, n: int) -> bool:
    if n == 1:
        return True

    def check(n):
        res = 0
        for i in str(n):
            res += int(i) ** 2
        return res

    hash_table = set()
    while n not in hash_table:
        hash_table.add(n)
        n = check(n)
        if n == 1:
            return True
    return False