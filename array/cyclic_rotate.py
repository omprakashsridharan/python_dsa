t = int(input())
res = []

for tc in range(t):
    n = int(input())
    arr = list(input().strip().split())
    last = arr[n - 1]
    i = n - 1
    while i >= 1:
        arr[i] = arr[i - 1]
        i = i - 1
    arr[0] = last
    res.append(" ".join(arr))

for r in res:
    print(r)
