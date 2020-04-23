def solution(strings, n):
    answer = []
    for i in range(len(strings)):
        #그렇다면 여기에서 [strings] 리스트에서 n번째 값을 인덱싱을 사용해 끄집어낼 수 있는 방법은 없을까?
        strings[i] = strings[i][n]+strings[i]
        # 바로 이 리스트에서 n 번째 요소를 불러오기 위해 [n]을 붙여 준 것이다.
        strings.sort()
    for j in range(len(strings)):
         answer.append(strings[j][1:])
    return answer

