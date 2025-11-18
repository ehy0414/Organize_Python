def solution(x):
    answer = True
    x_num = 0
    x = str(x)
    for i in range(len(x)):
        x_num += int(x[i])
        
    if(int(x) % x_num == 0):
        answer = True
    else:
        answer = False
    return answer