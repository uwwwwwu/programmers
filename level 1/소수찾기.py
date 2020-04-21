from itertools import permutations, combinations

def solution(numbers):
    answer = 0
    for i in range(1,len(numbers)):
    permute = permutations(numbers, i)
    print(list(permute))



# 소수 판별기
def isPrime(a):
    if a < 2:
        return False
    else:
        for i in range(2,a):
            if a % i == 0:
                return False
            else:
                return True


from itertools import permutations
answer = 0
def solution(numbers):

    for i in range(1,len(numbers)):
        # permute = set(list(map("".join,permutations(numbers,i))))

        permute = list(map("".join,permutations(numbers,i+1)))

        print(permute)
    a = permute
def is_prime(a: int)
    if a < 2:
        return False
    else:
        for i in range(3,a,2):
            if a % i == 0:
                return False
            else:
                answer += 1

# T 자형으로 공부하기

# 다양한 분야로 공부보기,
# 그중에 하고싶은 분야를 깊게 파기!

# 근데 프로그래밍 언어는 기반이다. 즉, 모든것을 공부하기위해 언어를 선행하는것이 좋다
# map zip, set, cycle 2중배열 등등