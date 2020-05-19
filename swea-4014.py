'''
swea 4014번 활주로 건설
링크: https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWIeW7FakkUDFAVH&
풀이 방법
- 구현만 잘하면 되는 문제이다.
- 활주로가 내리막 / 오르막 / 평지 일경우로 나누고 각 경우마다 조건을 확인해주면 된다.
'''
# 한 줄이 활주로인 경우
def check(row, x):

    count = 1
    before = row[0]

    for i in range(1,len(row)):
        # 내리막
        if row[i] < before: 
            #  높이차가 2보다 클경우
            if before-row[i] > 1:
                return 0
            else:
                # 범위를 벗어난 경우
                if i+x > len(row):
                    return 0
                else:
                    # 경사로가 제대로 만들어 질 수 있는지
                    for j in range(i, i+x): 
                        if row[j] != row[i]:
                            return 0
                    # 루프 돈만큼 마이너스 해줘야함
                    count = -x+1
        # 오르막
        elif row[i] > before:
            # 높이차가 2보다 클 경우
            if row[i]-before > 1:
                return 0
            else:
                # 그전까지 count했던 것으로 활주로 생성할 수 있으면
                if count >= x:
                    count = 1
                else:
                    return 0
        # 평지
        else:
            count+=1
        before = row[i]
    return 1

import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    answer = 0

    # 입력 받기
    N, X = map(int, input().split())
    MAP = [list(map(int, input().split())) for x in range(N)]

    # 각 행에 경사로를 건설할 수 있는지 살펴보기
    for row in MAP:
        answer += check(row, X)
    
    for col in zip(*MAP):
        answer += check(col, X)
 
    print('#{} {}'.format(test_case, answer))
