def solution(t, p):
    answer = 0
    for i in range(len(t)):
        if t[i:i+len(p)] <= p and len(p) == len(t[i:i+len(p)]):
            answer += 1
        else:
            pass
    return answer