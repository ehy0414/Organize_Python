def solution(s):
    answer = True
    if len(s) != 4 and len(s) != 6:
        return False
    for i in range(len(s)):
        if ord(s[i]) <= 64:
            pass
        else:
            return False
    return answer