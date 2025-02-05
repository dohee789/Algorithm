# ord() : return ASCII <-> chr() : return string
# print(ord('a')) -> 97
# print(chr(97)) -> 'a'

def find_max_occurred_alphabet(string):
    alphabet_occurred_array = find_alphabet_occurrence_array(string)
    max_occurred = 0
    max_occurred_alphabet = 0
    for i in range(len(alphabet_occurred_array)): # index 번째를 ASCII 로 변환 하기 위해 range 사용
        if alphabet_occurred_array[i] > max_occurred:
            max_occurred = alphabet_occurred_array[i]
            max_occurred_alphabet = chr(ord('a') + i) # 97 + index 를 변환 (c 가 최빈값 이라면 97 + c의 index 2)

    return  max_occurred_alphabet

def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26  # alphabet 총 개수인 26개의 0으로 배열 만들기

    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord('a') # char 이 a라면 97-97 = 0, b라면 98-97 = 1
        alphabet_occurrence_array[arr_index] += 1 # string 을 조회 하면서 arr_index 가 담길 때마다 0으로 채운 배열의 arr_index 번째에 +1 해주면 alphabet 의 빈도를 찾을 수 있음

    return alphabet_occurrence_array

print("정답 = c / 현재 풀이 값 = ", find_max_occurred_alphabet("aaa bb cccc d"))
print("정답 = o / 현재 풀이 값 = ", find_max_occurred_alphabet("i am a good boy"))