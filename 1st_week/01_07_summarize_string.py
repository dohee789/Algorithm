input_str = "aabcdd"

def summarize_string(input_str):
    alphabet_occurrence = [0]*26
    summarize_string = "" # summarized_string_list = []
    for i in input_str:
        occurred = ord(i) - ord('a')
        alphabet_occurrence[occurred] += 1

    for i in range(len(alphabet_occurrence)) :
        if alphabet_occurrence[i] > 0:
            if summarize_string:
                summarize_string += "/"
            summarize_string += chr(ord('a') + i) + str(alphabet_occurrence[i])
            # summarized_string_list.append(chr(ord('a') + i) + str(alphabet_occurrence[i]))
    return summarize_string
    # return "/".join(summarized_string_list)

print(summarize_string(input_str))


def summarize_string(target_string):
    n = len(target_string)
    count = 0
    result_str = ''

    for i in range(n - 1):
        print("i: ", i)
        if target_string[i] == target_string[i + 1]:
            print("target_string[i]: ", target_string[i])
            print("target_string[i+1]: ", target_string[i + 1])
            count += 1
        else:
            print("target_string[i]: ", target_string[i])
            print("count: ", count)
            result_str += target_string[i] + str(count + 1) + '/'
            print("result_str: ", result_str)
            count = 0

    result_str += target_string[n - 1] + str(count + 1)

    return result_str