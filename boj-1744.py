'''
백준 1744번 수 묶기
링크: https://www.acmicpc.net/problem/1744
풀이방법
- 수학 풀듯이 경우의 수 생각
- 정렬하여 음수끼리 곱 양수끼리 곱
- 0 과 1의 경우 예외를 잘 생각해주면 된다.
'''

from sys import stdin

stdin = open("input.txt", "r")

# 숫자 개수
N = int(stdin.readline())

numbers = [int(stdin.readline()) for _ in range(N)]

numbers.sort()
answer = 0
left = 0
right = N - 1

if N == 1:
    print(numbers[0])
else:
    # 음수
    i = 0
    while left < right:
        if numbers[left] < 1 and numbers[left+1] < 1:
            answer += (numbers[left] * numbers[left+1])
            left += 2
        else:
            break
    # 양수
    while right > 0:
        if numbers[right] > 1 and numbers[right-1] > 1:
            answer += (numbers[right] * numbers[right-1])
            right -= 2
        else:
            break
    # print(numbers, left, right)
    # 나머지
    answer += sum([numbers[i] for i in range(right, left-1, -1)])

    print(answer)
    
