def estimate_pages():
    n = 1
    while True:
        total_digits = 0
        digits = 1
        while digits <= n:
            total_digits += n // digits
            digits *= 10
        if total_digits == 1095:
            return n
        n += 1
print(estimate_pages())
