'''
링크: https://programmers.co.kr/learn/courses/30/lessons/42583
풀이방법
- queue로 bridge를 선언한다.
- queue에 
- edge들을 크루스칼 알고리즘으로 Minimum Spanning Tree를 찾는다.
'''

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = [0] * bridge_length # 다리 
    current_weight = 0 # 다리 현재 무게
    
    # 트럭들 전부 보내기
    while truck_weights:
        time += 1
        out = queue.pop(0)
        current_weight -= out
        
        # 트럭이 들어올 때 다리 최대 무게 점검
        # 트럭이 다리를 지나갈 수 없으면 0으로 bridge에 올린다.
        if current_weight + truck_weights[0] > weight:
            bridge.append(0)
        # 트럭이 다리를 지나갈 수 있으면 truck 뽑아서 queue에 올린다.
        # 현재 무게도 추가
        else:
            truck = truck_weights.pop(0)
            bridge.append(truck)
            current_weight += truck
    
    # 남은 트럭이 없을 경우
    # 현재 무게가 0이 될때 까지 bridge에 남은 truck들을 제거해준다.
    while curr_weight > 0:
        time += 1
        out = bridge.pop(0)
        current_weight -= bridge_out

    return time