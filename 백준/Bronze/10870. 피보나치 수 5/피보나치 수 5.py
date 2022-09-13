def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        ans = fibo(n-1) + fibo(n-2)
        return ans

print(fibo(int(input())))