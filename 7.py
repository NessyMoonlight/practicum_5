# n-quantity of stations, k-Artem's station,
# m-station need to arrive
n, k, m = map(int, input().split())

if m > k:
    print(m - k - 1)
elif m < k:
    print(n - k + (m - 1))
else:
    print(0)

