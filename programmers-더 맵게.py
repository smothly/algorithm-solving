import heapq

def solution(scoville, K):
    
    answer = 0
    scoville.sort()
    
    while True:
        # heapq를 사용하면 맨 앞에 변수가 제일 작은 변수가 됨
        if scoville[0] >= K:
            return answer
        
        # 길이가 1이 되면 K 이상으로 만들 수 없음
        elif len(scoville) == 1:
            return -1
        
        # 섞기: 가장 낮은 + (두번째 낮은 * 2)
        else:
            first = heapq.heappop(scoville)
            second = heapq.heappop(scoville)
            new_scovil = first + (second * 2)
            
            heapq.heappush(scoville, new_scovil)
            answer += 1
        
    return answer