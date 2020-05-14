'''
링크: https://programmers.co.kr/learn/courses/30/lessons/42895#
풀이방법
- 각 자릿수만큼 set을 만든 후 가능한 모든 연산을 수행한다.
- 잘 이해가 안됨...
'''

def solution(N, number):
    # set 초기화(8이 maximum)
    s = [ set() for x in range(8) ] 
    # 5, 55, 555 이런식으로 set만들어 줌
    for i, x in enumerate(s, start=1):
        x.add( int( str(N) * i ) )
    
    
    # 각 set loop 돌기
    for i in range(1, 8):
        
        for j in range(i):
            # s[j]는 첫번째 수
            # s[i-j-1] 두번째 수 i(전체 개수) - j(현재 개수) - 1 
            # 모든 연산을 다 하는 것이다.
            for op1 in s[j]:
                for op2 in s[i-j-1]:
                    s[i].add(op1 + op2)
                    s[i].add(op1 - op2)
                    s[i].add(op1 * op2)
                    if op2 != 0:
                        s[i].add(op1 // op2)
            
        if number in s[i]:
            answer = i + 1
            break
    else:
        answer = -1

    return answer