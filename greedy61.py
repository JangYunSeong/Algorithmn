n, k =input().split()
n = int(n)
k = int(k)

ans = 0

while bin(n).count('1') > k:
    idx = bin(n)[::-1].index('1')
    ans += 2**idx
    n += 2**idx
print(ans)