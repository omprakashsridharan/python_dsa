t = int(input())
res = []


def python_split(arr):
    orig = arr[:d]
    remaining = arr[d:]
    return remaining + orig


def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


def juggle_algo(arr, n, d):
    d = d % n
    g_c_d = gcd(d, n)
    for i in range(g_c_d):
        temp = arr[i]
        j = i
        while True:
            k = j + d
            if k >= n:
                k = k - n
            if k == i:
                break
            arr[j] = arr[k]
            j = k
        arr[j] = temp
    return arr


for tc in range(t):
    n, d = map(int, input().strip().split())
    arr = list(input().strip().split())
    # result = python_split(arr)
    result = juggle_algo(arr, n, d)
    res.append(" ".join(result))

for r in res:
    print(r)
