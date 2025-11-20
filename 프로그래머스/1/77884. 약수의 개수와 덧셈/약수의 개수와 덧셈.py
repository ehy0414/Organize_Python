def solution(left, right):
    cnt = 0
    result = 0
    for i in range(left, right+1):
        for j in range(1, i+1):
            if i % j == 0:
                cnt += 1
            else: 
                pass
        if cnt % 2 == 0:
            result += j
            cnt = 0
        else:
            result -= j
            cnt = 0
    return result