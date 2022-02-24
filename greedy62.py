from re import L


def fact(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

n,k = input().split()
n = int(n)
k = int(k)
# nHk = (k+n-1)Cn 9C6 = 9!/6!*3!
ans = fact(n+k-1) / (fact(k-1) * fact(n))
print(int(ans) % 1000000000)
