'''
링크: https://programmers.co.kr/learn/courses/30/lessons/42898
풀이방법
- Dynamic Programming
- i,j번째 위치는 i-1, j 와 i, j-1의 경우의 수를 더한 값이 된다.
- 초기화에서 1줄 씩 더 길게 해주는 것이 포인트이다.
'''

def solution(m, n, puddles):
    
    # MAP 초기화 시작지점은 1로 넣어준다.
    MAP = [[0 for i in range(m+1)] for _ in range(n+1)]
    MAP[1][1] = 1
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            # 시작 부분
            if i == j == 1:
                continue  
            # 웅덩이일 경우
            elif [j, i] in puddles:
                MAP[i][j] = 0
            # 웅덩이가 아닐 경우
            # 왼쪽과 위쪽에서 오는 경우의 수 더하기
            else:
                MAP[i][j] = MAP[i-1][j] + MAP[i][j-1]
    
    return MAP[-1][-1] % 1000000007