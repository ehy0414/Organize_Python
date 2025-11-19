def solution(a, b):
    answer = 0
    s = 0
    t = 0
    if a > b:
        s, t = b, a
    else:
        s, t = a, b
    for i in range(s,(t+1)):
        answer += i
    return answer