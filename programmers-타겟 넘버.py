'''
링크: https://programmers.co.kr/learn/courses/30/lessons/43165
풀이방법
- DFS 재귀적으로
'''



def solution(numbers, target):
    # 종료조건: 더 이상 갈 곳이 없고 마지막 값이 0이면
    if not numbers and target == 0 :
        return 1
    # 종료조건: 더 이상 갈 곳이 없으면
    elif not numbers:
        return 0
    # -, +두개로 재귀 돌림
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])

