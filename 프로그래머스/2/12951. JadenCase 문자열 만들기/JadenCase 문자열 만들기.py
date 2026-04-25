def solution(s):
    listStr = s.split(" ")
    result = []
    for i in range(len(listStr)):
        result.append(listStr[i].capitalize())
        
    return " ".join(result[0:])
