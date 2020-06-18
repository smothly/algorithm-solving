import re
def solution(files):
    # 1. 숫자 기준으로 분리 해준다.
    temp = [re.split(r"([0-9]+)", s) for s in files]
    # 2. 분리된 파일명을 head와 숫자 기준으로 정렬한다.
    sort = sorted(temp, key = lambda x: (x[0].lower(), int(x[1])))
    # 3. sort한 걸 다시 합쳐주기
    return ["".join(s) for s in sort]