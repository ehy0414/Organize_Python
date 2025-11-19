def solution(arr, divisor):
    answer = sorted([arr[i] for i in range(len(arr)) if arr[i] % divisor == 0])
    if answer == []:
        answer.append(-1)
    return answer