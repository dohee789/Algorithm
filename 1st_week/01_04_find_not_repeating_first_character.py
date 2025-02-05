# def find_not_repeating_first_character(string):
#     occurred = []
#     # 각 문자의 ASCII 값에서 'a'의 ASCII 값을 뺀 결과를 리스트에 추가
#     # occurred = [ord(char) - ord('a') for char in string]
#     for char in string:
#         value = ord(char) - ord('a')  # 문자 → 숫자로 변환
#         occurred.append(value)  # 리스트에 추가
#
#     # 첫 번째로 중복되지 않는 값 찾기
#     for i in range(len(occurred)):
#         if occurred.count(occurred[i]) == 1:  # 해당 값이 리스트에서 1번만 등장하는 경우
#             return chr(occurred[i] + ord('a'))  # 다시 문자로 변환하여 반환
#
#     return None  # 모든 문자가 중복되었다면 None 반환
#
# -> 반복문 안에서 count() 호출로 인해 O(n²)

def find_not_repeating_first_character(string):
    alphabet_array = [0] * 26

    # 각 문자의 빈도수 계산
    for char in string:
        index = ord(char) - ord('a')
        alphabet_array[index] += 1

    # 원본 문자열을 순회하며 첫 번째로 빈도수가 1인 문자 반환
    for char in string:
        index = ord(char) - ord('a')
        if alphabet_array[index] == 1:
            return char
    return "_"

# -> O(n) + O(n)
result = find_not_repeating_first_character
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 = b  현재 풀이 값 =", result("abcdacd"))
print("정답 = e 현재 풀이 값 =", result("racecar"))
print("정답 =_ 현재 풀이 값 =", result("aaaaaaaa"))