from math import gcd # 최소공배,최대공약수 https://brownbears.tistory.com/454
def solution(n, m):
    return [gcd(n,m), n*m/gcd(n,m)]
