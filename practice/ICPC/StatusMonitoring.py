n, m, t = map(int, input().split())

arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

for i in range(1, t + 1):
    max_count = 0
    min_count = 100000
    for j in range(m):
        temp = sum(1 for k in range(n) if arr[k][j] == i)
        max_count = max(max_count, temp)
        min_count = min(min_count, temp)
    print(min_count, max_count)
