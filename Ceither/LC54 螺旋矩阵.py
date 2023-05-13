def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    ans = []
    m = len(matrix)
    n = len(matrix[0])
    if m == 1:
        return matrix[0]
    if n == 1:
        return [line[0] for line in matrix]

    ltr = n - 1
    rtl = 0
    utd = m - 1
    dtu = 0

    deiection = 0
    total = m * n
    i = j = 0
    while total > 0:
        total -= 1
        ans.append(matrix[i][j])
        if deiection == 0:
            j += 1
            if j == ltr:
                deiection = 1
                dtu += 1
        elif deiection == 1:
            i += 1
            if i == utd:
                deiection = 3
                ltr -= 1
        elif deiection == 2:
            i -= 1
            if i == dtu:
                deiection = 0
                rtl += 1
        elif deiection == 3:
            j -= 1
            if j == rtl:
                deiection = 2
                utd -= 1
    return ans