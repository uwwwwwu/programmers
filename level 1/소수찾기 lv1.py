def solution(n):
    sieve = [True] * (n+1)

    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           # i가 소수인 경우
            for j in range(2*i, n+1, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    return len([i for i in range(2, n+1) if sieve[i] == True])

# def solution(n):
#     checker = 0
#     answer = 0
#     for i in range(2,n+1):
#         for j in range(2,i):
#             if i%j == 0:
#                 checker += 1
#         if checker == 0:
#             answer += 1
#         checker = 0
#     return answer

# def solution(n):
#     answer = 0
#     if n == 2 or n==3
#         answer+=1
#     if n % 2 is 0 or n % 3 is 0:
#         pass
#     for i in range(3, n, 2):
#         if n % i is 0:
#             pass
#         else:
#             answer+=1
#     return answer
# print("i:",i)
