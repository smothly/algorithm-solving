'''
링크: https://programmers.co.kr/learn/courses/30/lessons/17681?language=python3
풀이방법
- 비트연산자
- 또는 조건만 잘 검사하면 된다.
'''

def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n):
        s1 = bin(arr1[i])[2:]
        while len(s1) != n:
            s1 = '0' + s1 
        
        s2 = bin(arr2[i])[2:]
        while len(s2) != n:
            s2 = '0' + s2
            
        row = ''
        for j in range(n):
            if s1[j] == '1' or s2[j] == '1':
                row += '#'
            else:
                row += ' '
                
        answer.append(row)    
        
    return answer

'''
눈여겨볼만한 풀이
비트연산자로 계산하고 rjust로 0채운다.
'''
def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0')
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer