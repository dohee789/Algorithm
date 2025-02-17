def josephus_problem(n, k):
    result_arr = [] # 제거된 사람의 순서를 저장할 리스트

    next_index = k - 1 # 제거할 사람의 인덱스
    people_arr = list(range(1, n + 1)) # 현재 남아 있는 사람들의 리스트 (1부터 8을 range해야 1~7이 됨))

    while people_arr: # people_arr이 빈 리스트가 될 때까지 계속 반복
        result = people_arr.pop(next_index) # next_index 위치의 사람을 제거하고
        result_arr.append(result) # 그 사람을 result_arr에 추가
        if len(people_arr) != 0:
            next_index = (next_index + (k - 1)) % len(people_arr)

    print("<", ", ".join(map(str, result_arr)), ">", sep='')


n, k = map(int, input().split()) # 공백으로 구분된 입력값을 읽어 `n`, `k`에 정수로 저장
josephus_problem(n, k)