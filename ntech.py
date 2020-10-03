def solution(flowers):
    
    answer = 0
    # sort 
    flowers.sort(key=lambda x:(x[0], x[1]))
    
    new_days = []
    # 겹치는 부분을 합치는 과정 
    for i in range(len(flowers)-1):
        if flowers[i][1] >= flowers[i+1][0]:
            new_days.append((flowers[i][0], flowers[i+1][1]))
        else:
            new_days.append((flowers[i][0], flowers[i][1]))
        
    print(new_days)
    
    return sum(new_days, key=lambda x: x[1] - x[0])


    
    
def solution(histogram):
    
    start, end = 0, len(histogram) - 1
    answer = 0
    while True:
        print(start, end)
        if histogram[end-1] > histogram[end]:
            end -= 1
        elif histogram[start+1] > histogram[start]:
            start += 1
        else:
            answer = (end - start - 1) * min([histogram[start], histogram[end]])
            break
        
    return answer


def solution(N):
    answer = 0
    
    if N <= 2:
        return N
    
    dp = [1, 2]
    for i in range(2, N):
        dp.append(2 * dp[i-1] + i -1)
    print(dp)
    return dp[-1]

solution(6)