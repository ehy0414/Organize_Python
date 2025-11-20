def solution(phone_number):
    answer = ''
    answer = "*" * (len(phone_number) - 4)
    phone_number = phone_number[-4:]
    return answer + phone_number