from itertools import permutations

def solution(n, weak, dist):
    
    lenw = len(weak)
    lend = len(dist)
    
    # weak을 늘려서 초기화 해주는 과정 [1 5, 6, 10] + [12, 17, 18, 22] 
    for i in range(lenw):
        weak.append(weak[i]+n)
    
    print(weak)
    answer = lend + 1 # 최대 친구 수 + 계산 불가
    
    for i in range(lenw):
        # 새로 검사할 리스트 만들기: [1 5, 6, 10] + [13, 17, 18]중에 뽑아서
        new_list = weak[i:i+lenw]
        # 친구 순서 정하기, 모든 순서 탐색
        perm = permutations(dist, lend)
        for order in perm:
            index, count = 0,1 # 시작 인덱스, 친구 수
            possible_check_len = new_list[0] + order[index] # 첫 친구가 체크할 수 있는 범위
            for i in range(lenw):
                print(order, i, possible_check_len, count)
                # 확인가능 최대 거리를 넘을 경우
                if new_list[i] > possible_check_len:
                    # 다음 친구 투입
                    count += 1
                    index += 1
                    
                    # 친구 초과할 경우 
                    if count > len(order):
                        break

                    # 다음 친구 최대 거리
                    possible_check_len = new_list[i] + order[index]
                    
            # min값 계속 유지
            answer = min(answer, count)
            
    # 정답이 없을 경우
    if answer > lend:
        return -1
    return answer
