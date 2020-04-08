# import string
#
# def solution(s):
#     lt = string.ascii_letters
#     if lt in s:
#         return False
#     else:
#         return True


# import re
# def solution(s):
#     sutza = re.findall("\d+", s)
#     Sutza = ','.join(list(sutza))
#     if Sutza == s:
#         return True
#     else:
#         return False
# 5번 6번 틀림

'''
범위 지정
import re


def solution(s):
    if len(s) > 6 or len(s) < 4:
        return False

    sutza = re.findall("\d+", s)
    Sutza = ','.join(list(sutza))
    if Sutza == s:
        return True
    else:
        return False

근데 여전히 5번 실패
'''

# import re
#
#
# def solution(s):
#     if len(s) > 6 or len(s) < 4 and len(s) is not 5:
#         return False
#
#     sutza = re.findall("\d+", s)
#     Sutza = ','.join(list(sutza))
#     if Sutza == s:
#         return True
#     else:
#         return False
# # 혹시나 하고 길이 5도 제외했는데 실패!
#
# import re
# def solution(s):
#     sutza = re.findall("\d+", s)
#     Sutza = ','.join(list(sutza))
#     if len(s) ==4 or len(s) == 6:
#         if Sutza == s:
#             return True
#         else:
#             return False
#
#
# def solution(s):
#     if len(s) == 4 or len(s) == 6:
#         return s.isdigit()
#
#
# def solution(s):
#     return len(s) == 4 or len(s) == 6 and s.isdigit()
#
# 아예 구조 자체를 뜯어 고치니 바로됨
def solution(s):
    return (len(s) == 4 or len(s) == 6) and s.isdigit()

#
# 이거도 됨
import re
def solution(s):
    if (len(s) > 6 or len(s) < 4) or len(s) == 5:
        return False

    sutza = re.findall("\d+", s)
    Sutza = ','.join(list(sutza))
    if Sutza == s:
        return True
    else:
        return False
