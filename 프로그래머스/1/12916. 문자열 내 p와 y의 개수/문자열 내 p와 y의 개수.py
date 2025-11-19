def solution(s):
    p_cnt = 0
    y_cnt = 0
    s = s.lower()
    for i in range(len(s)):
        if s[i] == "p":
            p_cnt += 1
        elif s[i] == "y":
            y_cnt += 1

    return p_cnt == y_cnt