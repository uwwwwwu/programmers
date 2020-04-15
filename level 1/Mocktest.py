def solution(answers):
    answer = []

    # 찍는 방식
    firstst = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5] # 이 학생은 5개씩 반복적으로 찍는 습관이 있다..
    secondst = [2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5] # 이 학생은 8개씩
    thirdst = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5]# 얘는 10개씩 (고수)
    # 찍어나온 점수
    f_score = 0
    s_score = 0
    t_score = 0
    for i in range(len(answers)):
        if answers[i] == firstst[i % 5]: #그래서 이렇게 i % 찍는 패턴
            f_score += 1
        if answers[i] == secondst[i % 8]:
            s_score += 1
        if answers[i] == thirdst[i % 10]:
            t_score += 1

    # 가장 잘찍는 친구 찾기

    beststudent = max(f_score,s_score,t_score)

    if beststudent == f_score:
        answer.append(1)
    if beststudent == s_score:
        answer.append(2)
    if beststudent == t_score:
        answer.append(3)
    return answer
# 가장 잘찍는 친구 찾기
