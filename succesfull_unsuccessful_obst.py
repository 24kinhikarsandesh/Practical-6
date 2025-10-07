def OBST(p, q):
    n = len(p)
    e = [[0] * (n + 1) for _ in range(n + 2)]
    w = [[0] * (n + 1) for _ in range(n + 2)]
    root = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 2):
        e[i][i - 1] = q[i - 1]
        w[i][i - 1] = q[i - 1]

    for length in range(1, n + 1):  
        for i in range(1, n - length + 2):
            j = i + length - 1
            e[i][j] = float('inf')
            w[i][j] = w[i][j - 1] + p[j - 1] + q[j]
          
            for k in range(i, j + 1):
                cost = e[i][k - 1] + e[k + 1][j] + w[i][j]
                if cost < e[i][j]:
                    e[i][j] = cost
                    root[i][j] = k

    return e[1][n], root


p = [0.1, 0.2, 0.4, 0.3]
q = [0.05, 0.1, 0.05, 0.05, 0.1]

min_cost, root = OBST(p, q)
print(f"Expected output : {min_cost:.4f}")
