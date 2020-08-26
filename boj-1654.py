'''
백준 1654번 랜선 자르기
링크: https://www.acmicpc.net/problem/1654
풀이방법
- 이분 탐색
'''

from sys import stdin

# stdin = open("input.txt", "r")
# K: 기존에 가지고 있는 랜선의 개수
# N: 필요한 랜선의 개수 
K, N = map(int, stdin.readline().split())

# K개의 선 입력
lines = [int(stdin.readline()) for _ in range(K)]

# 이분탐색
# 구하고자 하는 것: 최대 랜선의 길이(정답)
# 이분 탐색의 기준: 랜선의 개수
start = 1
end = max(lines)

# start가 end보다 커지는 경우
while start <= end:

    # mid: 현재 랜선의 길이
    mid = (start + end) // 2

    # 각 랜선에서 만들 수 있는 선의 개수 구하기
    line_count = sum([line // mid for line in lines])

    # 선의 개수가 N보다 크면
    # 최소 선의 길이를 늘려야 함
    if line_count >= N:
        start = mid + 1

    # 위에 말과 반대
    elif line_count < N:
        end = mid - 1
    
print(end)