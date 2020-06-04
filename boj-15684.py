'''
백준 15684번 사다리 조작
링크: https://www.acmicpc.net/problem/15684
풀이방법
- DFS를 통한 완전탐색
- 3일때 종료하는 조건을 잘 해야한다.
- 연속되는 선은 안된다... 
'''

# 정답이 맞는지 확인하는 과정
def check():
    for start in range(N):
        end = start
        for i in range(H):
            if lines[i][end] == 1:
                end += 1
            elif end > 0 and lines[i][end-1]:
                end -= 1
        if start != end:
            return False
    return True

def solve(count, x, y):
    global answer
    if answer <= count:
        return
    # 정답이면
    if check():
        answer = min(answer, count)
        return
    # 3이면 종료
    if count == 3:
        return
    # 라인 하나씩 추가하면서 완전 탐색
    for i in range(x, H):
        # 첫번쨰 시작점
        if i == x:
            k = y
        else:
            k = 0
        # 세로축 번호
        # 라인놓을 세로축 찾기
        for j in range(k, N-1):
            if lines[i][j] == 1:
                j += 1
            else:
                lines[i][j] = 1
                solve(count+1, i, j+2) # 왜 j + 2냐면 다음라인은 사용 못하기 떄문
                lines[i][j] = 0


import sys
# sys.stdin = open("input.txt", "r")

# 입력
N, M, H = map(int, input().split())

lines = [[0]* N for _ in range(H)]
# line 만들기
for _ in range(M):
    x, y = map(int, input().split())
    lines[x-1][y-1] = 1

answer = 4
solve(0, 0, 0)
print(answer if answer < 4 else -1)