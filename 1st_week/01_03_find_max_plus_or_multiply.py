def find_max_plus_or_multiply(array):
    plus_or_multiply_sum = 0
    for num in array:
        if num <= 1 or plus_or_multiply_sum <= 1: # num 이 0,1 경우 다음 수와 곱하는 연산 보다 더하는 연산이 큼
            plus_or_multiply_sum += num # plus_or_multiply_sum 이 0,1 경우 또한 다음 num 과 곱하는 연산 보다 더하는 연산이 큼
        else:
            plus_or_multiply_sum *= num

    return plus_or_multiply_sum

result = find_max_plus_or_multiply
print("정답 = 728 현재 풀이 값 =", result([0,3,5,6,1,2,4]))
print("정답 = 8820 현재 풀이 값 =", result([3,2,1,5,9,7,4]))
print("정답 = 270 현재 풀이 값 =", result([1,1,1,3,3,2,5]))