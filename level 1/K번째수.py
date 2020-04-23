def solution(array, commands):
    answer = []
    for cmd in commands:
        i = cmd[0]
        j = cmd[1]
        k = cmd[2]
        slicing = array[i-1:j]
        slicing.sort()
        answer.append(slicing[k-1])
    return answer