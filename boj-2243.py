'''
백준 2243번 사탕상자
링크: https://www.acmicpc.net/problem/2243
풀이방법
- 세그먼트 트리 - 아직 코드가 명확히 이해 안됨 다시 공부할 예정
'''

import sys
sys.stdin = open("input.txt", "r")
tree = [0] * (1 << 21) # 2의 21승
bn = 1 << 20

# segment
def add(rank, count):
    tree[bn + rank] += count
    now = (bn + rank) // 2
    while now:
        tree[now] = tree[now*2] + tree[now*2+1]
        now = now//2

def pop_candy(d):
    now = d
    idx = 1
    while(now):
        if bn <= idx:
            print(idx - bn)
            add(idx-bn, -1)
            return
        elif tree[idx*2] >= now:
            idx *= 2
        else:
            now -= tree[idx*2]
            idx = idx*2+1

# 입력
N = int(input())

for i in range(N):
    command = list(map(int, sys.stdin.readline().split()))
    # 사탕을 끄내는 경우
    if command[0] == 1:
        pop_candy(command[1])
    # 사탕을 집어넣는 경우
    else:
        add(command[1], command[2])



'''
# import bisect
import heapq
# 입력
N = int(input())

candy = []

for i in range(N):
    command = list(map(int, sys.stdin.readline().split()))
    # 사탕을 끄내는 경우
    if command[0] == 1:
        # 여기선 순위를 넣는다.
        print(candy[command[1] - 1])
        candy.remove(candy[command[1] - 1])

    # 사탕을 넣는 경우
    elif command[0] == 2:
        if command[2] > 0:
            # 양수일 경우 집어넣는다.
            # for _ in range(command[2]):
            candy = list(heapq.merge(candy, [command[1]] * command[2]))
        else:
            # 음수일 경우 뺀다
            # 여기선 맛을 넣는다.
            index = candy.index(command[1])
            del candy[index:index+abs(command[2])]
'''