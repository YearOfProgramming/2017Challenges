
times = 0
def change(total, p, n, d, q):
    global times
    sum = p + n + d + q
    if sum == total:
        #print("q:{} d:{} n:{} p:{}".format(q // 25, d // 10, n // 5, p))
        times += 1
        return
    elif sum > total:
        return
    else:
        change(total, p, n, d, q + 25)
        change(total, p, n, d + 10, q)
        change(total, p, n + 5, d, q)
        change(total, total - q - n - d, n, d, q)  # should only have max of 1 depth

change(150, 0, 0, 0, 0)
print(times)