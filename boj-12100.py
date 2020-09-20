'''
백준 12100번 2048(Easy)
링크: https://www.acmicpc.net/problem/12100
풀이방법
- 구현에 구현에 구현이다.

출처: https://m.post.naver.com/viewer/postView.nhn?volumeNo=27593285&memberNo=33264526
'''

# 4가지 방향
# ^ 위: 0
# v 아래: 1 
# < 왼쪽: 2
# > 오른쪽: 3
def move(_map, direction, count):

    global answer
    after_move = [] # 합쳐진 후에 배열을 담기 위한 변수

    # 위 => 왼쪽 / 아래 => 오른쪽으로 처리하기위해 transpose를 해준다.
    if direction == 0 or direction == 1:
        _map = list(zip(*_map))

    # 각 row를 끄내서 합치기
    for i in range(len(_map)):
        each_row = _map[i]
        # 0 이 아닌 항목들만 뽑기
        non_zero = [_ for _ in each_row if _ != 0]
       
        # 왼쪽으로 합치기
        if direction == 0 or direction == 2:
            for row_i in range(len(non_zero) - 1):
                # 현재 값이 다음 값과 같으면
                if non_zero[row_i] == non_zero[row_i + 1]:
                    non_zero[row_i] += non_zero[row_i + 1]
                    non_zero[row_i + 1] = 0
            
            # 0인 부분들 제거
            non_zero = [_ for _ in non_zero if _ != 0]
            # 남은 길이 만큼 0으로 맞춰주기
            non_zero.extend([0] * (len(_map) - len(non_zero)))
        
        # 오른쪽으로 합치기
        else:
            for row_i in range(len(non_zero)-1, 0, - 1):
                # 현재 값이 다음 값과 같으면
                if non_zero[row_i] == non_zero[row_i - 1]:
                    non_zero[row_i] += non_zero[row_i - 1]
                    non_zero[row_i - 1] = 0
                
            # 0인 부분들 제거
            non_zero = [_ for _ in non_zero if _ != 0]
            # 남은 길이 만큼 0으로 맞춰주기
            temp_zero = list([0] * (len(_map) - len(non_zero)))
            temp_zero.extend(non_zero)
            non_zero = temp_zero
        
        # 추가!
        after_move.append(non_zero)

    
    # transpose 다시 원복
    if direction == 0 or direction == 1:
        after_move = list(zip(*after_move))

    # 5일 경우 종료
    if count == 5:
        answer = max(answer, max(map(max, after_move)))
        return
    # 아닐경우 계속 4방향 이동
    else:
        for i in range(4):
            move(after_move, i, count+1)


from sys import stdin
stdin = open("input.txt", "r")
# N: 맵의 크기
N = int(stdin.readline())

MAP = [list(map(int, stdin.readline().split())) for _ in range(N)]

answer = 0

# 4가지 방향으로 탐색
for i in range(4):
    move(MAP, i, 1)

print(answer)