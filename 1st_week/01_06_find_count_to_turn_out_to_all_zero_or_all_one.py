"""
모두 0으로 만들거나 모두 1로 만들어야 함
0->1로 바뀌는 횟수 즉, 모두 1로 바꿀때의 횟수
1->0으로 바뀌는 횟수 즉, 모두 0으로 바꿀때의 횟수
비교해서 최솟값을 찾기
"""

input = "101110"
def find_count_to_turn_out_to_all_zero_or_all_one(string):
    count_to_all_one = 0
    count_to_all_zero = 0

    #아래 for 문은 첫번째 인덱스 요소의 뒤집기 여부부터 판단하기 때문에 0번째 비교도 필요함
    if string[0] == '0': # 0번째 인덱스의 요소가 0 이라면 1로 모두 바꿔주는 경우일테니
        count_to_all_one += 1
    elif string[0] == '1': # 0번째 인덱스의 요소가 1 이라면 0으로 모두 바꿔주는 경우일테니
        count_to_all_zero += 1

    for i in range(len(string) - 1): # 문자열의 인덱스번째 요소 끼리 비교하기 위해 인덱스번째 -1 만큼 돌아야함
        if string[i] != string[i+1]: # 앞뒤로 비교해서 다르다면 뒤집어야 하는 순간이라는 것
            if string[i+1] == "0": # 뒤집어야 하는 인덱스 요소가 0인지 1인지에 따라 구분
                count_to_all_one += 1 # 0이라면 모두 1로 바꾸겠다는 것
            elif string[i+1] == "1":
                count_to_all_zero += 1 # 1이라면 모두 0으로 바꾸겠다는 것
    print(count_to_all_one, count_to_all_zero)
    return min(count_to_all_one, count_to_all_zero)


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)