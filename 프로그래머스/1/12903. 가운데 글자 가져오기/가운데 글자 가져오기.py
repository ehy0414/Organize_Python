def solution(s):
    answer = ''
    sub = int(len(s) / 2)
    if len(s) % 2 == 0:
        answer = s[sub-1:sub+1]
    else:
        answer = s[sub]
    return answer