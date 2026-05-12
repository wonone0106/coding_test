def solution(phone_book):
    phone_set = set(phone_book)
    
    for phone in phone_book:
        for i in range(1, len(phone)):   # 각 번호의 모든 접두어 확인
            if phone[:i] in phone_set:
                return False
    return True