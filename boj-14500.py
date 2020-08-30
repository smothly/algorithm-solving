'''
백준 14500번 테트로미노
링크: https://www.acmicpc.net/problem/14500
풀이방법
- DFS
- 백트래킹
- 구현
'''

def dfs(x, y, value, length):
    
    global answer

    # dfs 종료 조건
    if length >= 4:
        answer = max(answer, value)
        return
    
    # 4방향 체크
    for d in direction:
        nx = x + d[0]
        ny = y + d[1]
        if 0 <= nx < N and 0 <= ny < M and not visit[nx][ny]:

            visit[nx][ny] = True # 방문 체크

            # 다음지점 value 더하고 length 더해서 호출
            dfs(nx, ny, value+MAP[nx][ny], length+1)

            visit[nx][ny] = False # 방문 체크 해제

def exception_check(x, y, value):

    global answer
    # ㅏ ㅜ ㅓ ㅗ 순으로 체크 0,0
    # 점은 가장 1. 왼쪽 2. 상단에 있다고 판단.
    if 0 <= x+2 < N and 0 <= y+1 < M: # ㅏ
        value = MAP[x][y] + MAP[x+1][y] + MAP[x+2][y] + MAP[x+1][y+1]
        answer = max(answer, value)

    if 0 <= x+1 < N and 0 <= y+2 < M: # ㅜ
        value = MAP[x][y] + MAP[x][y+1] + MAP[x][y+2] + MAP[x+1][y+1]
        answer = max(answer, value)
    
    if 0 <= x-1 and x+1 < N and 0 <= y+1 < M: # ㅓ
        value = MAP[x][y] + MAP[x-1][y+1] + MAP[x][y+1] + MAP[x+1][y+1]
        answer = max(answer, value)

    if 0 <= x-1 and 0 <= y+2 < M: # ㅗ
        value = MAP[x][y] + MAP[x][y+1] + MAP[x][y+2] + MAP[x-1][y+1]
        answer = max(answer, value)


from sys import stdin
stdin = open("input.txt", "r")
# 입력
N, M = map(int, stdin.readline().split())
MAP = [list(map(int, stdin.readline().split())) for _ in range(N)]

direction = ((-1, 0), (1, 0), (0, -1), (0, 1)) # ^ > v < 순
visit = [[False] * M for _ in range(N)]
answer = 0

for i in range(N):
    for j in range(M):

        # 시작지점도 방문 체크 해제 필요
        visit[i][j] = True

        dfs(i, j, MAP[i][j], 1)

        visit[i][j] = False

        # ㅜ 모양의 경우 dfs로 체크가 불가능해서 따로 처리.
        exception_check(i, j, MAP[i][j])

print(answer)

