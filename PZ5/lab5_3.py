def super_fibonacci(n,m):
    list_F = []
    elem = 0
    for i in range(m):
        list_F.append(1)
    if n > m:
        for j in range(n-m):
            for k in range(m):
                elem += list_F[j+k]
            list_F.append(elem)
            elem = 0
    return (list_F[-1])
