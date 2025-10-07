def OBST(p):
    n = len(p)
    C = [[0] * (n + 2) for _ in range(n + 2)]
    R = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):   ## successful
        C[i][i - 1] = 0
        C[i][i] = p[i - 1]
        R[i][i] = i
    C[n + 1][n] = 0

    for d in range(1, n):
        for i in range(1, n - d + 1):
            j = i + d
            minval = float('inf')
            for k in range(i, j + 1):
                cost = C[i][k - 1] + C[k + 1][j]
                if cost < minval:
                    minval = cost
                    kmin = k
            R[i][j] = kmin
            summ = sum(p[i - 1:j]) 
            C[i][j] = minval + summ

    return C[1][n], R


p = [0.1, 0.2, 0.4, 0.3]
min_cost, root = OBST(p)
print(f"Expected Cost : {min_cost:.4f}")
