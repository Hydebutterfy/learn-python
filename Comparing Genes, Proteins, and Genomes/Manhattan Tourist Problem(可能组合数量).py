def q(n,m):
    if m==0:
        return 1
    if n==0:
        return 1
    return q(n-1,m)+q(n,m-1)

print(q(16,12))
 # 买哈顿街道走道组合。