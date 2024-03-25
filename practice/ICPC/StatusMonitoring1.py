n, m, t = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

counts = [[0] * t for _ in range(m)]
for i in range(n):
    for j in range(m):
        counts[j][arr[i][j] - 1] += 1

for i in range(t):
    min_count = min(counts[j][i] for j in range(m))
    max_count = max(counts[j][i] for j in range(m))
    print(min_count, max_count)
