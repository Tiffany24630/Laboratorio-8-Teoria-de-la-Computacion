def problema1(n):
    counter = 0

    for i in range(n // 2, n + 1):
        for j in range(1, n - n // 2 + 1):
            k = 1

            while k <= n:
                counter += 1
                k *= 2

    return counter