'''
링크: https://programmers.co.kr/learn/courses/30/lessons/12987
풀이 방법
- 매번 검사하면 시간초과가 뜬다.
- 둘다 sort한 채로 a를 이길 수 있는 최소의 b를 찾으며 한번의 loop로 해결한다.
'''


def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    j = 0
    # 둘다 sort한 채로 비교하면
    # a를 이길 수 있는 b가 가장 작은 수가 된다.
    for i in range(len(A)):
        if A[j] < B[i]:
            answer = answer + 1
            j = j+1

    return answer