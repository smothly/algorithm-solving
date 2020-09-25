def solution(number, k):
    stack = [number[0]]
    for num in number[1:]:
        while len(stack) > 0 and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        stack.append(num)

    # 마지막 테스트 케이스
    # 제거 횟수를 다 사용하지 못하면 stack에서 나머지 짤라줌
    if k != 0: 
        stack = stack[:-k]

    return ''.join(stack)