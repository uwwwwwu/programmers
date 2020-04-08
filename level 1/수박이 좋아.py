def solution(n):
    s = "수"
    for a in range(2,n+1 ):
        if a % 2 == 0:
            s +="박"
        else:
            s +="수"
    return s


