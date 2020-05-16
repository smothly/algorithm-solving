'''
링크: https://programmers.co.kr/learn/courses/30/lessons/43162
풀이방법
- BFS
- 전부 다 방문할 때까지 방문하지 않은 노드들을 탐색한다.
'''


def solution(n, computers):
    answer = 0
    bfs = []
    visited = [0]*n

    # 전부 방문할 때 까지
    while 0 in visited:
        # 방문하지 않은 노드 끄내기
        x = visited.index(0)
        bfs.append(x)
        visited[x] = 1

        # 시작노드부터 갈 수 있는 경우 = 1개의 네트워크
        while bfs:
            node = bfs.pop()
            visited[node] = 1
            for i in range(n):
                if visited[i] == 0 and computers[node][i] == 1:
                    bfs.append(i)
                    visited[i] = 1
        answer += 1
    return answer