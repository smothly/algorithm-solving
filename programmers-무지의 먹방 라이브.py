'''
프로그래머스 무지의 먹방 라이브 2019 kakao blind recruitment
링크: https://programmers.co.kr/learn/courses/30/lessons/42891
풀이방법
- 가장 작은 음식들을 cycle을 계산하여 제거한다.
- 아이디어를 생각하는 건 쉬웠으나.. 코드로 구현하는데 애먹음..
- 참고: https://inspirit941.tistory.com/entry/Python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-2019-%EC%B9%B4%EC%B9%B4%EC%98%A4-recruit-%EB%AC%B4%EC%A7%80%EC%9D%98-%EB%A8%B9%EB%B0%A9-%EB%9D%BC%EC%9D%B4%EB%B8%8C-Level-3
'''


import heapq
def solution(food_times, k):
    # (음식 크기, 원판에서의 위치) 로 food_times 재정의
    food_times = [(food, idx) for idx, food in enumerate(food_times, 1)]
    # heapify. 음식 크기가 작은 순으로 뽑아낸다.
    heapq.heapify(food_times)
    
    # 가장 크기 작은 음식
    small_food = food_times[0][0]
    prev_food = 0
    # 작은 음식을 완전히 소비하기 위해 원판을 완주할 수 있는 경우
    while k - ((small_food - prev_food) * len(food_times)) >= 0:
        # 해당 음식을 완전히 소비하는 데 걸린 시간만큼 뺀다
        k -= (small_food - prev_food) * len(food_times)
        prev_food, index = heapq.heappop(food_times)
        if not food_times:
            return -1
        small_food = food_times[0][0]
    
    food_times = sorted(food_times, key = lambda x: x[1])  
    
    return food_times[k % len(food_times)][1]