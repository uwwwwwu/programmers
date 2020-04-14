import datetime
WeekDay=['MON','TUE','WED','THU','FRI','SAT','SUN']
def solution(a, b):
    return WeekDay[datetime.datetime(2016,a,b).weekday()]
    # 데이트타임 모듈 써서 문제를 풀어보았습니다.
    # 사실 이런 방법도 좋지만 모듈을 쓰지않는 쪽이 공부에는 도움이 될까하여 모듈없이 다시 해보겠씁니다.
    # 죄송합니다. 못하겠습니다..