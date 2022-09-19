# 유클리드 호제법

# 최대공약수
def gcd(a, b):
    while b != 0:
        a, b = b, a % b   # a가 b보다 작아도 첫번째 연산에서 바뀜
    return a

# 최소공배수
def lcm(a, b):
    return a*b // gcd(a, b)

m, n = map(int, input().split())
print(gcd(m, n))
print(lcm(m, n))
