def solution(s):
    return sorted(s)
# 입력값 〉	"Zbcdefg"
# 기댓값 〉	"gfedcbZ"
# 실행 결과 〉	실행한 결괏값 ['Z', 'b', 'c', 'd', 'e', 'f', 'g']이(가) 기댓값 'gfedcbZ'와(과) 다릅니다.
# 문자열 합치는 작업필요!


def solution(s):
    return "".join(sorted(s))
# 테스트 1
# # 입력값 〉	"Zbcdefg"
# # 기댓값 〉	"gfedcbZ"
# # 실행 결과 〉	실행한 결괏값 'Zbcdefg'이(가) 기댓값 'gfedcbZ'와(과) 다릅니다.
# 순서 바꾸는거 필요!!


def solution(s):
    return "".join(sorted(s)[::-1])
# 테스트 1
# 입력값 〉	"Zbcdefg"
# 기댓값 〉	"gfedcbZ"
# 실행 결과 〉	테스트를 통과하였습니다.
# 야호!!! 신난다!