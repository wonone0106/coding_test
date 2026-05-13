from itertools import permutations

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    candidates = set()
    
    # 1자리부터 len(numbers)자리까지 모든 순열 생성
    for r in range(1, len(numbers) + 1):
        for perm in permutations(numbers, r):
            num = int(''.join(perm))
            candidates.add(num)
    
    return sum(1 for n in candidates if is_prime(n))