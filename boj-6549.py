import sys
sys.stdin = open("input.txt","rt")
if __name__ == "__main__" :
    while True :
        ##print("#####")
        tmp = list(map(int,input().split())) + [0] ## 마지막 요소에 0을 넣어 뒤의 while문에서 stack에 남아있는 값을 남김없이 처리 가능하게 된다.
        N = tmp[0] ## 갯수
        if N == 0 :
            break
        s = [(1,tmp[1])] ## stack : 저장 형태 : (인덱스번호, 높이)
        answer = 0
        for i in range (2,N+2) :
            ##print(s)
            cur = i
            while s and s[-1][1] > tmp[i] : ## 스택에 숫자가 있고, 마지막 요소가 현재의 높이보다 큰 경우
                print(s)
                cur,h = s.pop()
                answer = max(answer,(i-cur)*h) ## 값 갱신
            ## 위의 while문에 의해 stack은 s[x][1]에 대해 오름차순으로 정렬된다.
            s.append((cur,tmp[i])) ## 이렇게 저장하면 -> tmp[i]의 높이를 곱할 수 있는 가능한 좌표의 최소값이 같이 저장된다.
        print(answer)