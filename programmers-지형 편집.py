'''
링크: https://programmers.co.kr/learn/courses/30/lessons/12984/
풀이방법
- 모든 경우의 수를 구하면 time limit이 된다.
- height를 정렬하여 min -> max까지 loop돌며 O(n)으로 한번에 해결한다.
- 규칙은 height가 증가하는 만큼 p랑 q를 계산하면 된다
'''

def solution(land, P, Q):
    
    answer = -1
        
    height_list = [land[i][j] for i in range(len(land)) for j in range(len(land))]
    height_list.sort() # 높이 순으로 정렬

    # 가장 낮은 높이 기준으로 맞출 때 금액 계산
    temp = 0
    for i in range(len(height_list)):
        temp += (height_list[i]-height_list[0])*Q  
    answer = temp

    # height가 min일 때 부터 max일 때까지 차례로 계산한다.
    print(height_list)
    for i in range(1, len(height_list)):
        down = i             # i번째 블럭
        up = len(height_list) - i      # i번째 블럭 이후로 남은 블럭 갯수
        # print(i, height_list[i], temp, down, up)
        temp += down * (height_list[i] - height_list[i-1]) * P  # v[i]로 만들기 위한 블럭 추가 비용
        temp -= up * (height_list[i] - height_list[i-1]) * Q # v[i]로 만들기 위한 블럭 제거 비용 반환
        if answer > temp:
            answer = temp
    return answer   