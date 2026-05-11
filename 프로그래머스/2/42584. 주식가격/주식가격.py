def solution(prices):
    answer = [0] * len(prices)
    stack = []  # 인덱스를 저장

    for i, price in enumerate(prices):
        # 현재 가격이 스택 top보다 낮으면 → 가격 하락
        while stack and prices[stack[-1]] > price:
            j = stack.pop()
            answer[j] = i - j  # 떨어진 시점까지의 시간
        stack.append(i)

    # 스택에 남은 건 끝까지 안 떨어진 것
    while stack:
        j = stack.pop()
        answer[j] = len(prices) - 1 - j

    return answer