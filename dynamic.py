d = [0] * 1000

def dp(x):
    global d
    if(x == 1):
        return 1
    if(x == 2):
        return 2
    if(d[x] != 0):
        return d[x]
    d[x] = dp[x-1] + dp[x-2] % 10007

a = int(input('insert the number :'))
print(dp(a))