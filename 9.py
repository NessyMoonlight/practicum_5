h = list(map(int, input().split()))

maxH = max(h)
minH = min(h)
middleH = sum(h) - maxH - minH

print(maxH, middleH, minH)
